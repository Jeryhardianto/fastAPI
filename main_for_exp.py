from fastapi import FastAPI
from pydantic import BaseModel, parse_obj_as, Field, BeforeValidator
from typing import Optional, List, Annotated

from enum import Enum
import pymongo


app = FastAPI()

# connect to mongodb
client = pymongo.MongoClient("mongodb+srv://myuser:mysecret@cluster0.l6crrms.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

# create database and collection
db = client.get_database("mydatabase")
# create collection
transactions = db.get_collection("transactions")


# enum
class TipeEnum(str, Enum):
    def __str__(self):
        return str(self.value)
    INCOME = "INCOME"
    EXPENSE = "EXPENSE"
    PURCHASE = "PURCHASE"
    INVESTMENT = "INVESTMENT"

# pydantic model transaction
class Transaction(BaseModel):
    tipe: TipeEnum
    amount: int
    description: Optional[str] 

# Represents an ObjectId field in the database.
PyObjectId = Annotated[str, BeforeValidator(str)]

# Model schema for transactions
class Transaction(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    tipe: TipeEnum
    amount: int
    description: Optional[str] 

    class Config:
        json_encoders = {PyObjectId: str}

# =========================================================================

# Get Request
@app.get("/transactions")
def get_transactions():
    return {"data": transactions}
    
# Get Request with Query Parameters 
@app.get("/transactionswithparams")
def get_transactions(tipe: str, amount: int):
    return {"data": "Type: " + tipe + " Amount: " + str(amount)}

# Get Request with Path Parameters
@app.get("/transactionspath/{tipe}")
def get_transactions(tipe: str):
    return {"data": "Type: " + tipe }

# Get Request with Filter
@app.get("/transactionswithfilter")
def get_transactions(tipe:Optional[TipeEnum] = None):
    if tipe:
        result = transactions.find({"tipe": tipe})
    else:
        result = transactions.find({})
    result = list(result)
    return {"data": parse_obj_as(List[Transaction], result)}


# =================================================================================
# Post Request
# Post Request with Query Parameters
@app.post("/transactions")
def insert_transactions(tipe: str, amount: int, description: str):
    data_transaction = {"tipe": tipe, "amount": amount, "description": description}
    transactions.append(data_transaction)
    return {"data": data_transaction}
    
# Post Request with pydantic model / BaseModel
@app.post("/transactionspydantic")
def insert_transactions(input_transaction: Transaction):
    transactions.insert_one(input_transaction.dict())
    return {"data": input_transaction}


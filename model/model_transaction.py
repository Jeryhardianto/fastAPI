from typing import Optional
from bson import ObjectId
from pydantic import BaseModel, Field

from enums.enum_tipe import TipeEnum
from model.model_common import PyObjectId

# Model schema for transactions
class Transaction(BaseModel):
    id: PyObjectId = Field(alias="_id")
    tipe: TipeEnum
    amount: int
    description: Optional[str] 

    class Config:
        json_encoders = {ObjectId: str}
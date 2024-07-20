from fastapi import Depends
from pymongo.database import Database
from config.config import get_db_connection
from typing import List
from pydantic import TypeAdapter

from dto.dto_transaction import InputTransaction
class RepositoryTransaction:
  def __init__(self, db:Database = Depends(get_db_connection)):
     self.respository = db.get_collection("transactions")
  
  def insert_new_transaction(self, new_transaction: InputTransaction):
    return self.respository.insert_one(new_transaction.model_dump())
  
  def get_transactions(self, match_filters = dict):
    result = self.respository.find(match_filters)
    result = list(result)

    return TypeAdapter(List[InputTransaction]).validate_python(result)
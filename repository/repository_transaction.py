from fastapi import Depends
from pymongo.database import Database
from config.config import get_db_connection
from typing import List
from pydantic import parse_obj_as

from dto.dto_transaction import InputTransaction
from model.model_transaction import Transaction
class RepositoryTransaction:
  def __init__(self, db:Database = Depends(get_db_connection)):
     self.repository = db.get_collection("transactions")
  
  def insert_new_transaction(self, new_transaction: InputTransaction):
    return self.repository.insert_one(new_transaction.model_dump())
    
  def get_list_transaction(self, match_filter: dict, skip: int, size: int):
    result = self.repository.find(match_filter).skip(skip).limit(size)
    result = list(result)
    return parse_obj_as(List[Transaction], result)

  def count_list_transaction(self, match_filter: dict):
    return self.repository.count_documents(match_filter)
  
  def export_list_transaction(self, match_filter: dict, projection_stage: dict):
    result = self.repository.find(match_filter, projection_stage)
    result = list(result)
    return result
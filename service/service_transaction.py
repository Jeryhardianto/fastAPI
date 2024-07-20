from typing import Optional
from dto.dto_transaction import InputTransaction
from repository.repository_transaction import RepositoryTransaction
from fastapi import Depends
from enums.enum_tipe import TipeEnum

class ServiceTransaction:
   def __init__(self, repository_transaction: RepositoryTransaction = Depends())->None:
       self.repository_transaction = repository_transaction

   def insert_new_transaction(self, input_transaction: InputTransaction):
       return self.repository_transaction.insert_new_transaction(input_transaction)
   
   def get_list_transactions(self, tipe: Optional[TipeEnum] = None):
       match_filters = {}

       if tipe is not None:
           match_filters['tipe'] = tipe

       return self.repository_transaction.get_transactions(match_filters)
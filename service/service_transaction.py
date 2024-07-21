import math
from typing import Optional
from dto.dto_transaction import InputTransaction, OutputTransactionPage
from dto.dto_common import TokenData
from model.model_transaction import Transaction
from repository.repository_transaction import RepositoryTransaction
from fastapi import Depends
from enums.enum_tipe import TipeEnum

class ServiceTransaction:
   def __init__(self, repository_transaction: RepositoryTransaction = Depends())->None:
       self.repository_transaction = repository_transaction

   def insert_new_transaction(self, input_transaction: InputTransaction, current_user: TokenData):
        new_transaction = Transaction(
            tipe=input_transaction.tipe,
            amount=input_transaction.amount,
            description=input_transaction.description,
            user_id=current_user.userId,
        )
        return self.repository_transaction.insert_new_transaction(new_transaction)
   
   def get_list_transaction(
        self, tipe: Optional[TipeEnum] , page: int, size: int, current_user: TokenData
    ):
        match_filter = {"user_id": current_user.userId}
        if tipe is not None:
            match_filter["tipe"] = tipe
        skip = page * size
        total_data = self.repository_transaction.count_list_transaction(match_filter)
        list_transaction = self.repository_transaction.get_list_transaction(
            match_filter, skip, size
        )
        total_page = math.ceil(total_data / size)
        print(list_transaction)    
        return OutputTransactionPage(
            page=page,
            size=size,
            total_data=total_data,
            total_page=total_page,
            data=list_transaction,
        )
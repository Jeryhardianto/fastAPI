from typing import Optional
from fastapi import APIRouter, Depends

from dto.dto_transaction import InputTransaction
from enums.enum_tipe import TipeEnum
from service.service_transaction import ServiceTransaction

router_transaction = APIRouter(prefix="/api/v1", tags=["Transaction"])

@router_transaction.post("/transaction")
def insert_new_transactions(input_transaction: InputTransaction ,service_transaction: ServiceTransaction = Depends()):
  service_transaction.insert_new_transaction(input_transaction)
  return {"data": input_transaction}

@router_transaction.get("/transactions")
def get_list_transactions(tipe: Optional[TipeEnum] = None, service_transaction: ServiceTransaction = Depends()):
   return {"data": service_transaction.get_list_transactions(tipe)}
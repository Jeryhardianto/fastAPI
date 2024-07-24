from datetime import datetime
from typing import Optional
from fastapi.responses import StreamingResponse
from typing_extensions import Annotated
from fastapi import APIRouter, Depends

from dto.dto_common import TokenData
from dto.dto_transaction import InputTransaction
from enums.enum_tipe import TipeEnum
from model.model_common import InputDateGue
from service.service_common import get_current_user
from service.service_transaction import ServiceTransaction

router_transaction = APIRouter(prefix="/api/v1", tags=["Transaction"])

@router_transaction.post("/transaction")
def insert_new_transactions(
   input_transaction: InputTransaction,
   current_user: Annotated[TokenData, Depends(get_current_user)],
   service_transaction: ServiceTransaction = Depends()
):
  service_transaction.insert_new_transaction(input_transaction, current_user)
  return input_transaction

@router_transaction.get("/transactions")
def get_list_transaction(
    current_user: Annotated[TokenData, Depends(get_current_user)],
    tipe: Optional[TipeEnum] = None,
    page: int = 0,
    size: int = 10,
    service_transaction: ServiceTransaction = Depends(),

):
 return service_transaction.get_list_transaction(tipe, page, size, current_user)

@router_transaction.post("/export")
def export_history_transaction(
    current_user: Annotated[TokenData, Depends(get_current_user)],
    start_date: Optional[datetime] = None,
    end_date: Optional[datetime] = None,
    tipe: Optional[TipeEnum] = None,
    service_transaction: ServiceTransaction = Depends(),
):
    if start_date is None or end_date is None:
        start_date = None
        end_date = None
    else:
         # Check if start_date and end_date are not already datetime objects
        if not isinstance(start_date, datetime):
            start_date = datetime.strptime(start_date, "%Y-%m-%d")
        if not isinstance(end_date, datetime):
            end_date = datetime.strptime(end_date, "%Y-%m-%d")

    content_file, file_name = service_transaction.export_transaction(
        tipe, start_date, end_date, current_user
    )

    print(content_file)

    headers = {"Content-Disposition": f"attachment; filename={file_name}"}
    return StreamingResponse(iter([content_file]), headers=headers)
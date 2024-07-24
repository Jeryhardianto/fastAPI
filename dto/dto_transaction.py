from typing import Optional, List
from pydantic import BaseModel
from dto.dto_common import BasePage
from bson import ObjectId
from enums.enum_tipe import TipeEnum
from datetime import datetime
from model.model_transaction import Transaction
from util.util_date_time import convert_datetime_str

# pydantic model transaction
class InputTransaction(BaseModel):
    tipe: TipeEnum
    amount: int
    description: Optional[str] 

class OutputTransactionPage(BasePage):
    data: List[Transaction]

    class Config:
        json_encoders = {ObjectId: str, datetime: convert_datetime_str}
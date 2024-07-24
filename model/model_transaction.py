from datetime import datetime
from typing import Optional
from bson import ObjectId
from pydantic import BaseModel, Field

from enums.enum_tipe import TipeEnum
from model.model_common import PyObjectId
from util.util_date_time import convert_datetime_str


# Model schema for transactions
class Transaction(BaseModel):
    id: PyObjectId = Field(alias="_id", default_factory=ObjectId)
    created_time: datetime = Field(default_factory=datetime.now)
    tipe: TipeEnum
    amount: int
    description: Optional[str] 
    user_id: str

    class Config:
         json_encoders = {ObjectId: str, datetime: convert_datetime_str}
    
    @classmethod
    def project_export(cls):
        return {
            "_id": 0,
            "Tanggal Transaksi": "$created_time",
            "Tipe": "$tipe",
            "Nominal": "$amount",
            "Catatan": "$notes",
            "Metode": "$method",
        }
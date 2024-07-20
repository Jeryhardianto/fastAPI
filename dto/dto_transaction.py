from typing import Optional
from pydantic import BaseModel
from enums.enum_tipe import TipeEnum

# pydantic model transaction
class InputTransaction(BaseModel):
    tipe: TipeEnum
    amount: int
    description: Optional[str] 
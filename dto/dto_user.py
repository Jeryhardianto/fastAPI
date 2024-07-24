from pydantic import BaseModel
from enums.enum_tipe import TipeEnum

# pydantic model transaction
class InputUser(BaseModel):
    username: str
    password: str
    name: str

class InputLogin(BaseModel):
    username: str
    password: str
class OutputLogin(BaseModel):
    access_token: str
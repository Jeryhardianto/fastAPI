from pydantic import BaseModel


class StandardResponse(BaseModel):
    detail: str

class TokenData(BaseModel):
    userId: str
    name: str

class BasePage(BaseModel):
    page: int
    size: int
    total_data: int
    total_page: int
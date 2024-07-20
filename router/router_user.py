from fastapi import APIRouter, Depends, HTTPException

from dto.dto_user import InputLogin, InputUser
from service.service_user import ServiceUser


router_user = APIRouter(prefix="/api/v1", tags=["User"])

@router_user.post("/user")
def insert_new_user(input_user: InputUser ,service_user: ServiceUser = Depends()):
  service_user.insert_new_user(input_user)
  return {"data": input_user}


@router_user.post("/login")
def login_user(input_login: InputLogin, service_user: ServiceUser = Depends()):
  result = service_user.login_user(input_login)
  # user not found
  if result is None:
    raise HTTPException(401,  "Invalid username or password")
  return result
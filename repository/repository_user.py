from fastapi import Depends
from pymongo.database import Database
from config.config import get_db_connection

from dto.dto_user import InputLogin, InputUser
from model.model_user import User
class RepositoryUser:
  def __init__(self, db:Database = Depends(get_db_connection)):
     self.respository = db.get_collection("users")
  
  def insert_new_user(self, new_user: InputUser):
    return self.respository.insert_one(new_user.model_dump())
  
  def find_user_by_username_password(self, input_login: InputLogin):
    result = self.respository.find_one({"username": input_login.username, "password": input_login.password})

    if result is not None:
      return User.model_validate(result)
    return None

from dto.dto_user import InputUser
from repository.repository_user import RepositoryUser
from fastapi import Depends

class ServiceUser:
   def __init__(self, repository_user: RepositoryUser = Depends())->None:
       self.repository_user = repository_user

   def insert_new_user(self, input_user: InputUser):
       return self.repository_user.insert_new_user(input_user)
   
   def login_user(self, input_user: InputUser):
       return self.repository_user.find_user_by_username_password(input_user)
    
   
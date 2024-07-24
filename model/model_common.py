from bson import ObjectId
from pydantic import  BeforeValidator
from typing import Annotated

from util.util_date_time import convert_str_date

# Represents an ObjectId field in the database.
PyObjectId = Annotated[str, BeforeValidator(str)]



#  Create for validation date
InputDateGue = Annotated[str, BeforeValidator(convert_str_date)]

from fastapi import Depends
from typing_extensions import Annotated
from fastapi.security import OAuth2PasswordBearer

from dto.dto_common import TokenData
from service import service_jwt



oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/login")

def get_current_user(
        token: Annotated[str, Depends(oauth2_scheme)],
        service_jwt: service_jwt.ServiceJwt = Depends(),
):
    return TokenData.model_validate(service_jwt.decode_token(token))
from fastapi import FastAPI
from router.router_transaction import router_transaction
from router.router_user import router_user

app = FastAPI()

app.include_router(router_transaction)
app.include_router(router_user)


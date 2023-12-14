from fastapi import FastAPI
from .routers import auth, order

app = FastAPI()

app.include_router(auth.router)
app.include_router(order.router)

from fastapi import APIRouter

router = APIRouter(
    prefix="/orders",
    tags=['Orders']
)


@router.get("/")
def hello():
    return {"message": "order"}

from fastapi import APIRouter

router = APIRouter(
    prefix="/auth",
    tags=['Authentication']
)


@router.get("/")
def hello():
    return {"message": "auth"}

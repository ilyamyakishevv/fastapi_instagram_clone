from fastapi import APIRouter, Depends
from sqlalchemy.orm.session import Session

from db.database import get_db
from db import db_post
from routers.schemas import PostBase, PostDisplay


router = APIRouter(
    prefix="/post",
    tags=["Post"]
)

@router.post('/', response_model=PostDisplay)
def create_post(request: PostBase, db: Session = Depends(get_db)):
    return db_post.create(db, request)
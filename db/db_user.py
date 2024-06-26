from routers.schemas import UserBase
from db.models import DbUser
from sqlalchemy.orm.session import Session
from db.hashingpass import Hash


def create_user(db: Session, request: UserBase):
    new_user = DbUser(
        username=request.username,
        email=request.email,
        password=Hash.bcrypt(request.password)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get_user(db: Session, user_id: int):
    user =  db.query(DbUser).filter(DbUser.id == user_id).first()
    return user

def get_all_users(db: Session):
    return db.query(DbUser).all()
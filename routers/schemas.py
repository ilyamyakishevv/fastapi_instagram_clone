from pydantic import BaseModel


class UserBase(BaseModel):
    username: str
    email: str
    password: str


class UserDisplay(BaseModel):
    username: str
    email: str

    class Config(): 
        orm_mode = True


class PostBase(BaseModel):
    image_url: str
    image_url_type: str
    caption: str
    creater_id: int
    


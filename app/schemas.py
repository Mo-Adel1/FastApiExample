from datetime import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr, conint

class UserCreate(BaseModel):
    email: EmailStr
    password: str


class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime
    
    class Config:
        from_attributes=True


class PostBase(BaseModel):
    title: str
    content: str
    published: bool

class PostCreate(PostBase):
    pass

class Post(PostBase):
    id: int
    created_at: datetime
    owner: UserOut

    class Config:
        from_attributes=True

class PostOut(BaseModel):
    post: Post
    votes: int

class Token(BaseModel):
    access_token: str
    token_type:str

class TokenData(BaseModel):
    id: Optional[str]=None


class Vote(BaseModel):
    post_id: int 
    dir: conint(le=1)







# owner_id: UserOut


# post: Post --> # id: int + # title: str + # content: str + # published: bool = True + # created_at: datetime
# votes: int
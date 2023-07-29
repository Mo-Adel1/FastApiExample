from . import models
from .database import engine
from .routers import post, user, auth, vote
from . import swagger_config
from .config import settings
from fastapi.middleware.cors import CORSMiddleware
# models.Base.metadata.create_all(bind=engine) # tells the sqlalchemy to check the tables(models) and create them(if not exist) 

app = swagger_config.app

origins = []
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(post.router)
app.include_router(user.router)
app.include_router(vote.router) 
app.include_router(auth.router) 

@app.get("/")
def root(): 
    return {"message": "welcome"}
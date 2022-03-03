from fastapi import FastAPI
from . import models
from .database import engine
from .routers import post, user, auth

#Create database table
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Grabbing the router objects
app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)




 

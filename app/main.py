from pdb import post_mortem
from typing import Optional, List
from urllib import response
from fastapi import FastAPI, Response, status, HTTPException, Depends
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from . import api_schemas
from . import models
from .database import engine, get_db
from sqlalchemy.orm import Session
from . import utils
from .routers import post, user, auth

#Create database table
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

while True:

    try:
        conn = psycopg2.connect(host='localhost', database='fastapi', user='postgres',
                                password='2022301ab', cursor_factory=RealDictCursor)  # Get the column names
        cursor = conn.cursor()
        print("Database connection was succesfull!")
        break
    except Exception as error:
        print("Connection to the database failed")
        print("Error:", error)
        time.sleep(2)

# Grabbing the router objects
app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)




 

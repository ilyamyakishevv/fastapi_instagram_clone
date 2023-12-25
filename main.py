from fastapi import FastAPI
from db import models
from db.database import engine
from routers import user


app = FastAPI()
app.include_router(user.router)

@app.get("/")
def root():
    return "App is running, use endpoints (read the docs) for use it!"


models.Base.metadata.create_all(engine)

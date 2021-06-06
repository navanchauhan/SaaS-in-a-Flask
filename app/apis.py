from app import models
from api import app
from fastapi import Body, FastAPI, HTTPException
from fastapi.middleware.wsgi import WSGIMiddleware
from pydantic import BaseModel


@app.get("/version")
async def API_Version():
    return {"message": app.version}


@app.get("/v1/user-details")
async def API_User_Details(email: str):
    user = models.User.query.filter_by(email=email).first()
    try:
        assert user != None
    except AssertionError:
        raise HTTPException(status_code=404, detail="User Not Found")
    return {"first_name": user.first_name, "last_name": user.last_name}

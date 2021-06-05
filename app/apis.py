from api import app

from fastapi import Body, FastAPI
from fastapi.middleware.wsgi import WSGIMiddleware
from pydantic import BaseModel

@app.get("/version")
async def API_Version():
	return {"message":app.version}
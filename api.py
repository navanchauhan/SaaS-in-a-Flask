from app import app as flask_app
from fastapi import Body, FastAPI
from fastapi.middleware.wsgi import WSGIMiddleware
from pydantic import BaseModel


app = FastAPI(title="SaaS-in-a-Flask", description="Sample API", version="0.1")

from app import apis

app.mount("/", WSGIMiddleware(flask_app))

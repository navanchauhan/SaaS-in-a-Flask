import os

SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/test.db'
SQLALCHEMY_TRACK_MODIFICATIONS = False

SECRET_KEY = "tchtchtch"

ADMIN_EMAIL = "admin@example.com"
ADMIN_PASSWORD = "iamgroot"

GOOGLE_CLIENT_ID=os.environ.get("GOOGLE_CLIENT_ID2")
GOOGLE_CLIENT_SECRET=os.environ.get("GOOGLE_CLIENT_SECRET2")
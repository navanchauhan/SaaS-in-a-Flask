import os

SQLALCHEMY_DATABASE_URI = "sqlite:////tmp/test.db"
SQLALCHEMY_TRACK_MODIFICATIONS = False

SECRET_KEY = "tchtchtch"

ADMIN_EMAIL = "admin@example.com"
ADMIN_PASSWORD = "iamgroot"

GOOGLE_CLIENT_ID = os.environ.get("GOOGLE_CLIENT_ID")
GOOGLE_CLIENT_SECRET = os.environ.get("GOOGLE_CLIENT_SECRET")


# MAIL_BACKEND = 'file'
# MAIL_FILE_PATH = '/tmp/app-messages'
MAIL_BACKEND = "smtp"
MAIL_SERVER = os.environ.get("MAIL_SERVER")
MAIL_PORT = os.environ.get("MAIL_PORT")
MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
MAIL_FROM = os.environ.get("MAIL_FROM")
MAIL_USE_TLS = bool(os.environ.get("MAIL_USE_TLS"))

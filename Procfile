web: FLASK_APP=app python -m flask database create && FLASK_APP=app python -m flask database admin-create && gunicorn -w 4 api:app -k uvicorn.workers.UvicornWorker -b "0.0.0.0:$PORT"

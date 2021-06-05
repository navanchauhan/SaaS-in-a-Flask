web: flask database create && flask database admin-create && gunicorn -w 4 api:app -k uvicorn.workers.UvicornWorker -b "0.0.0.0:$PORT"

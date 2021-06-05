FROM python:3.8-slim AS builder

LABEL maintainer = "Navan Chauhan <navanchauhan@gmail.com>" \
	org.label-schema.name="SaaS-in-a-Flask" \
	org.label-schema.description="https://web.navan.dev/SaaS-in-a-Flask"

EXPOSE 5000

WORKDIR /saas-in-a-flask

COPY requirements.txt api.py ./
RUN pip install -r requirements.txt

COPY ./app ./app

RUN FLASK_APP=app flask database create
RUN FLASK_APP=app flask database admin-create 

CMD gunicorn -w 4 api:app -k uvicorn.workers.UvicornWorker -b "0.0.0.0:5000"
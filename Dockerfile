FROM python:3.8-slim AS builder

LABEL maintainer = "Navan Chauhan <navanchauhan@gmail.com>" \
	org.label-schema.name="SaaS-in-a-Flask" \
	org.label-schema.description="https://web.navan.dev/SaaS-in-a-Flask"

EXPOSE 5000

WORKDIR /saas-in-a-flask

COPY requirements.txt api.py ./
RUN apt-get update \
    && apt-get install -y --no-install-recommends gcc and-build-dependencies \
    && rm -rf /var/lib/apt/lists/* \
    && pip install -r requirements.txt \
    && apt-get purge -y --auto-remove gcc

COPY ./app ./app

RUN FLASK_APP=app flask database create
RUN FLASK_APP=app flask database admin-create 

CMD gunicorn -w 4 api:app -k uvicorn.workers.UvicornWorker -b "0.0.0.0:5000"
FROM python:3.8-alpine AS builder

LABEL maintainer = "Navan Chauhan <navanchauhan@gmail.com>" \
	org.label-schema.name="SaaS-in-a-Flask" \
	org.label-schema.description="https://web.navan.dev/SaaS-in-a-Flask"

EXPOSE 5000

WORKDIR /saas-in-a-flask

COPY simple-requirements.txt api.py ./
RUN apk add --no-cache --virtual .build-deps \
	build-base \
	cairo \
	cairo-dev \
	cargo \
	gcc \
	libffi-dev \
	openssl-dev \
	py-cffi \
	python3-dev \
	rust \
	&& pip install -r requirements.txt \
	&& find /usr/local \
        \( -type d -a -name test -o -name tests \) \
        -o \( -type f -a -name '*.pyc' -o -name '*.pyo' \) \
        -exec rm -rf '{}' + \
    && runDeps="$( \
        scanelf --needed --nobanner --recursive /usr/local \
                | awk '{ gsub(/,/, "\nso:", $2); print "so:" $2 }' \
                | sort -u \
                | xargs -r apk info --installed \
                | sort -u \
    )" \
    && apk add --virtual .rundeps $runDeps \
    && apk del .build-deps

COPY ./app ./app

RUN FLASK_APP=app flask database create
RUN FLASK_APP=app flask database admin-create 

CMD gunicorn -w 4 api:app -k uvicorn.workers.UvicornWorker -b "0.0.0.0:5000"
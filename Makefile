# Makefile

## Configuration

PROJECT := $(shell basename $(PWD))

## Install Dependencies
.PHONY: install
install:
	pip install -r requirements.txt

## Create Database
.PHONY: db
db:
	cd app && ln -sf config_dev.py config.py
	FLASK_APP=app python -m flask database create

## Start Dev Server with Hot-Reloading
.PHONY: dev
dev:
	cd app && ln -sf config_dev.py config.py
	FLASK_APP=app python -m flask run --reload --debugger --extra-files ./app/templates/base.html:./app/templates/contact.html:./app/templates/index.html	

## Create Self-Signed SSL Certificate
.PHONY: cert-create
cert-create:
	openssl req -x509 -newkey rsa:4096 -nodes -out cert.pem -keyout key.pem -days 365

## Dev server with SSL
.PHONY: dev-ssl
dev-ssl:
	cd app && ln -sf config_dev.py config.py
	FLASK_APP=app python -m flask run --reload --debugger --cert=cert.pem --key=key.pem 

## Gunicorn Server with Uvicorn worker for FastAPI Support
.PHONY: gunicorn
gunicorn:
	python -m gunicorn -w 1 api:app -k uvicorn.workers.UvicornWorker -b "0.0.0.0:8080" --reload

## Uvicorn Server
.PHONY: uvicorn
uvicoen:
	python -m uvicorn api:app --reload
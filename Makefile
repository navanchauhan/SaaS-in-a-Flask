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
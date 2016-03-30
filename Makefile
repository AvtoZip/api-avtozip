.PHONY: build clean devserver fasttest install install-py \
		lint manage migrate server shell test

# Project settings
LEVEL ?= development
PROJECT = avtozip

# Virtual environment settings
ENV ?= ./env
ifeq ($(LEVEL),development)
	REQUIREMENTS = -r requirements-dev.txt
else:
	REQUIREMENTS = -r requirements.txt
endif

# Python commands
COVERAGE = coverage
FLAKE8 = flake8
GUNICORN = gunicorn
PYTHON = python

# Gunicorn settings
GUNICORN_NAME ?= avtozip
GUNICORN_WORKERS ?= $(shell python -c "import multiprocessing; print(multiprocessing.cpu_count() * 2 + 1);")
LOGS_DIR ?= ./logs
SERVER_HOST ?= 0.0.0.0
SERVER_PORT ?= 8012

# Other settings
DJANGO_SERVER = runserver
DJANGO_SHELL = shell_plus
TEST_ARGS ?= avtozip

all: install build

build: migrate

clean:
ifeq ($(CIRCLECI),)
	find ./$(PROJECT) $(ENV) \( -name "*.pyc" -o -type d -empty \) -exec rm -rf {} +
endif

devserver: clean
	COMMAND="$(DJANGO_SERVER) $(SERVER_HOST):$(SERVER_PORT)" $(MAKE) manage

fasttest:
	REUSE_DB=1 $(MAKE) test

install: install-github-key install-py

install-github-key:
	ssh-keygen -H -F github.com > /dev/null || ssh-keyscan -H github.com >> ~/.ssh/known_hosts

install-py:
ifeq ($(CIRCLECI),)
	[ ! -d "$(ENV)/" ] && virtualenv $(ENV)/ || :
	$(ENV)/bin/pip install $(REQUIREMENTS)
else
	pip install $(REQUIREMENTS)
endif

lint:
ifeq ($(LEVEL),development)
	$(FLAKE8) --statistics ./$(PROJECT)/
endif

manage:
	$(PYTHON) ./$(PROJECT)/manage.py $(COMMAND)

migrate:
	COMMAND="migrate --noinput" $(MAKE) manage

server: clean lint
	PYTHONPATH=$(PROJECT) $(GUNICORN) -b $(SERVER_HOST):$(SERVER_PORT) -w $(GUNICORN_WORKERS) -n $(GUNICORN_NAME) -t 60 --graceful-timeout 60 $(gunicorn_args) $(GUNICORN_ARGS) $(PROJECT).wsgi:application

shell:
	COMMAND=$(DJANGO_SHELL) $(MAKE) manage

test: clean lint
	$(COVERAGE) run --branch ./$(PROJECT)/manage.py test $(TEST_ARGS)
	$(COVERAGE) report

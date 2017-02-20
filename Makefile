.PHONY: build checkmessages clean devserver fasttest install install-py install-bower static lint loaddata manage messages migrate server \
		shell test

# Project settings
LEVEL ?= development
PROJECT = avtozip

# Virtual environment settings
ENV ?= ./env
ifeq ($(LEVEL),development)
	REQUIREMENTS = -r requirements-dev.txt
else
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
TEST_ARGS ?= $(PROJECT)
TEST_PROCESSES ?= 4

all: install build

build: migrate loaddata

checkmessages:
	COMMAND="checkmessages --verbosity 3" $(MAKE) manage

clean:
ifeq ($(CIRCLECI),1)
	find ./$(PROJECT) $(ENV) \( -name "*.pyc" -o -type d -empty \) -exec rm -rf {} +
endif

devserver: clean
	COMMAND="$(DJANGO_SERVER) $(SERVER_HOST):$(SERVER_PORT)" $(MAKE) manage

fasttest:
	TEST_ARGS="$(TEST_ARGS) --keepdb --parallel $(TEST_PROCESSES)" $(MAKE) test

install: install-github-key install-py install-bower

install-github-key:
	ssh-keygen -H -F github.com > /dev/null || ssh-keyscan -H github.com >> ~/.ssh/known_hosts

install-py:
	pip install $(REQUIREMENTS)

install-bower:
	COMMAND="bower install" $(MAKE) manage

static:
	COMMAND="collectstatic" $(MAKE) manage

lint:
ifeq ($(LEVEL),development)
	$(FLAKE8) --statistics ./$(PROJECT)/
endif

loaddata:
	COMMAND="loaddata webstore/fixtures/test_store.json" $(MAKE) manage

manage:
	cd $(PROJECT) && $(PYTHON) ./manage.py $(COMMAND)

messages:
	COMMAND="makemessages --locale en --locale ru -v 1" $(MAKE) manage
	COMMAND="compilemessages --locale en --locale ru -v 1" $(MAKE) manage

migrate:
	COMMAND="migrate --noinput" $(MAKE) manage

server: clean lint
	PYTHONPATH=$(PROJECT) $(GUNICORN) -b $(SERVER_HOST):$(SERVER_PORT) -w $(GUNICORN_WORKERS) -n $(GUNICORN_NAME) -t 60 --graceful-timeout 60 $(gunicorn_args) $(GUNICORN_ARGS) $(PROJECT).wsgi:application

shell:
	COMMAND=$(DJANGO_SHELL) $(MAKE) manage

test: clean lint checkmessages
	$(COVERAGE) erase
	$(COVERAGE) run $(PROJECT)/manage.py test $(TEST_ARGS)
	$(COVERAGE) combine
	$(COVERAGE) report --show-missing

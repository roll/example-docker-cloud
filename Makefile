.PHONY: all build install list migrate push test


PROJECT := example


all: list

build:
	docker build -t $$IMAGE .

install:
	pip install --upgrade -r requirements.dev.txt

list:
	@grep '^\.PHONY' Makefile | cut -d' ' -f2- | tr ' ' '\n'

migrate:
	@echo 'database migration'

push:
	$${CI?"Push is avaiable only on CI/CD server"}
	docker login -e $$DOCKER_EMAIL -u $$DOCKER_USER -p $$DOCKER_PASS
	docker push $$IMAGE
	PROJECT=$(PROJECT) ENVIRONMENT=STAGING python scripts/push-stacks.py
	PROJECT=$(PROJECT) ENVIRONMENT=PRODUCTION python scripts/push-stacks.py

test:
	pylama messenger
	py.test

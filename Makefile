.PHONY: build train run test

build:
	docker-compose build

train:
	docker-compose run --rm api python train.py

run:
	docker-compose up api

mlflow:
	docker-compose up mlflow

test:
	docker-compose run --rm api pytest test_api.py

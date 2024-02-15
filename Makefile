.PHONY: run

run:
	poetry run flask --app ./app/ run

migrate:
	poetry run flask db migrate -m "$(msg)"

db_upgrade:
	poetry run flask db upgrade

db_downgrade:
	poetry run flask db downgrade

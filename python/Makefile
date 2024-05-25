.PHONY: default
default:
	@$(MAKE) -s new_env

.PHONY: new_env
new_env:
	@[ -n "$$(poetry run which python)" ] && source $$(poetry env info --path)/bin/activate && poetry env remove $$(which python) || true
	poetry install
	@[ -n "${VIRTUAL_ENV}" ] || exec poetry shell

.PHONY: test
test:
	pytest -rfE --doctest-modules tests/ --cov=KinkLink --cov-report=html --cov-report=term --cov-report=term-missing

.PHONY: format
format:
	@poetry run ruff check --select I --fix .
	@poetry run ruff format .

.PHONY: lint
lint:
	@poetry run ruff check .

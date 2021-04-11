.PHONY: clean-pyc clean-build

test:
	@pytest -s

coverage:
	@pytest --cov=flask_mistune

clean: clean-build clean-pyc

clean-build:
	@rm -fr build/
	@rm -fr dist/
	@rm -fr *.egg-info
	@rm -f mistune.c
	@rm -fr .coverage


clean-pyc:
	@find . -name '*.pyc' -exec rm -f {} +
	@find . -name '*.pyo' -exec rm -f {} +
	@find . -name '*~' -exec rm -f {} +
	@find . -name '__pycache__' -exec rm -fr {} +

.PHONY: build
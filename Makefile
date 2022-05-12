test:
	pipenv run pytest

test-coverage:
	pipenv run coverage run -m pytest
	pipenv run coverage report

deploy:
	pipenv run python setup.py sdist
	pipenv run twine upload dist/*

install:
	pipenv install

deploy-docs:
	pipenv run mkdocs gh-deploy

servce-docs:
	pipenv run mkdocs serve

run-%:
	pipenv run python examples/$*.py

shell:
	pipenv run ipython

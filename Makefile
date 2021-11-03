test:
	coverage run -m unittest -v
	coverage report -m

dist:
	python -m build

pypi: dist
	python -m twine upload dist/*

.PHONY: test dist pypi

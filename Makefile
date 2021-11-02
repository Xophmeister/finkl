test:
	python -m unittest -v

dist:
	python -m build

pypi: dist
	python -m twine upload dist/*

.PHONY: test dist pypi

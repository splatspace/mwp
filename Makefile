.PHONY: clean-pyc clean-build docs clean

clean-all: clean clean-venv

clean-venv:
	rm -rf bin/
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info
	rm -rf include/
	rm -rf lib/
	rm -rf local/
	rm -rf local/
	rm -rf share/

clean:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +

venv:
	virtualenv .

bin/python: venv

bin/pip: venv

dev: bin/python 
	bin/pip install -r requirements.txt
	bin/python setup.py develop

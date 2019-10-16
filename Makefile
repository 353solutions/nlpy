all:
	$(error please pick a target)

env:
	# Create venv directory if not exist
	test -d venv || virtualenv venv
	./venv/bin/python -m pip install -r requirements.txt

dev-env: env
	./venv/bin/python -m pip install -r requirements-dev.txt

test:
	find . -name '*.pyc' -exec rm -f {} \;
	./venv/bin/flake8 nlp tests
	./venv/bin/python -m pytest \
	    --doctest-modules \
	    --disable-warnings \
	    --verbose \
	    nlp tests

package:
	python setup.py sdist

clean:
	rm -rf build dist nlp.egg-info

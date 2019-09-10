run_unittests:
	echo "Starting unittests"
	python -m unittest discover

run_pytests:
	echo "Starting pytests"
	pytest -v --cov tests/

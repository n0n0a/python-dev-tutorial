.PHONY: unittest doctest

unittest:
	python -m unittest discover -v

doctest:
	python -m doctest -v FizzBuzz/*.py
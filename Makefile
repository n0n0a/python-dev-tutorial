.PHONY: unittest doctest install uninstall clean

unittest:
	python -m unittest discover -v

doctest:
	python -m doctest -v FizzBuzz/*.py


install:
	python setup.py install

uninstall:
	pip uninstall fizzbuzz -y

clean:
	rm -rf build
	rm -rf dist
	rm -rf *.egg-info
	find . name "*pychache*" | xargs rm -rf
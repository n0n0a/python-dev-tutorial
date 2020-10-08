from setuptools import setup, find_packages

setup(
    name='fizzbuzz',
    version="0.0.1",
    description='Fizz Buzz program.',
    author='n0n0a',
    url='https://github.com/n0n0a/python-dev-tutorial',
    author_email='n0n0a6262@gmail.com',
    license='MIT',
    install_requires=[],
    packages=find_packages(exclude=["tests"]),
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License"
    ]
)
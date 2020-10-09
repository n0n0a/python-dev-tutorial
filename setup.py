from setuptools import setup, find_packages

setup(
    name='fizzbuzz',
    version="0.0.4",
    description='Fizz Buzz program.',
    author='n0n0a',
    url='https://github.com/n0n0a/python-dev-tutorial',
    author_email='n0n0a6262@gmail.com',
    license='MIT',
    install_requires=["pytest", "click"],
    packages=find_packages(exclude=["tests"]),
    entry_points={
        'console_scripts': 'fizzbuzz-cli = FizzBuzz.fizzbuzz:main'
    },
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License"
    ]
)
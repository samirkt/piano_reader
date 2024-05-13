# setup.py
from setuptools import setup, find_packages


requirements = [
    "pygame",
]

setup(
    name="piano_reader",
    version="0.1",
    packages=find_packages(),
    test_suite="tests",
    install_requires=requirements,
)

#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

requirements = ["python-json-logger", "everett", "everett[ini]"]
test_requirements = ["pytest", "pytest-watch", "pytest-cov", "flake8", "flask", "flask_graphql", "flask_restful"]
setup_requirements = ["pytest-runner", "setuptools>=40.5.0"]

extras = {"test": test_requirements}

setup(
    name="cis_logger",
    version="0.0.1",
    author="Andrew Krug",
    author_email="akrug@mozilla.com",
    description="Mozilla IAM logger wrapper.",
    long_description=long_description,
    url="https://github.com/mozilla-iam/cis",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)",
        "Operating System :: OS Independent",
    ],
    install_requires=requirements,
    license="Mozilla Public License 2.0",
    include_package_data=True,
    packages=find_packages(include=["cis_logger"]),
    setup_requires=setup_requirements,
    tests_require=test_requirements,
    extras_require=extras,
    test_suite="tests",
    zip_safe=True,
)

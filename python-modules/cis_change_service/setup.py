#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

requirements = [
    'python-jose',
    'cryptography',
    'everett',
    'flask',
    'flask_cors',
    'boto>=2.36.0',
    'boto3>=1.6.16',
    'botocore>=1.12.13',
    'six',
    'cis_profile==0.0.3'
    # cis_publisher
]

setup_requirements = [
    'pytest-runner',
    'setuptools>=40.5.0'
]
test_requirements = ['pytest', 'pytest-watch', 'pytest-cov', 'patch', 'mock', 'flake8', 'moto>=1.3.7']

extras = {'test': test_requirements}

setup(
    name="cis_change_service",
    version="0.0.1",
    author="Andrew Krug",
    author_email="akrug@mozilla.com",
    description="Flask bindings for publishing profile changes using the auth0 authorizer.",
    long_description=long_description,
    url="https://github.com/mozilla-iam/cis",
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Mozilla Public License",
        "Operating System :: OS Independent",
    ),
    install_requires=requirements,
    license="Mozilla Public License 2.0",
    include_package_data=True,
    packages=find_packages(include=['cis_change_service']),
    scripts=['bin/cis_change_service'],
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    extras_require=extras,
    zip_safe=False
)

# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='__PROJECT-NAME__',
    version='0.1.0',
    description='Sample package for Python-Guide.org',
    long_description=readme,
    author='__USER-NAME__',
    author_email='__USER-MAIL-ADDRESSS__',
    url='https://github.com/__GITHUB-USER__/__PROJECT-NAME__',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)


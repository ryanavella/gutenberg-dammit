#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from setuptools import setup
from setuptools import find_packages

with open('README.md', encoding='UTF-8') as readme_file:
    readme = readme_file.read()

setup(
    name='gutenbergdammit',
    version='0.0.2',
    author='Allison Parrish',
    author_email='allison@decontextualize.com',
    url='https://github.com/aparrish/gutenbergdammit',
    description='Extract plain text and metadata from the GutenTag dump',
    long_description=readme,
    packages=find_packages(),
    install_requires=[
        'chardet',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        'Programming Language :: Python :: 3',
    ],
    platforms='any',
)

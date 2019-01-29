# -*- coding: utf-8 -*-
import sys
from setuptools import setup, find_packages

if sys.platform != 'darwin':
    sys.exit('airport-py depends on a specific mac os tool called "airport"')

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='airport-py',
    version='0.1.0',
    description='Mac OS X airport command result parser',
    long_description=readme,
    author='Egemen Yildiz',
    author_email='egemenyildiz.e@gmail.com',
    url='https://github.com/egemenyildiz/airport-py',
    license=license,
    packages=find_packages(),
    python_requires="<=2.7.15",
    classifiers=[
        'Programming Language :: Python :: 2 :: Only',
        'License :: OSI Approved :: MIT License',
        'Operating System :: MacOS :: MacOS X',
    ],
)

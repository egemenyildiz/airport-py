# -*- coding: utf-8 -*-
import sys
from setuptools import setup, find_packages

if sys.platform != 'darwin':
    sys.exit('airport-py depends on a specific mac os tool called "airport"')

setup(
    name='airport-py',
    version='0.1.1',
    description='Mac OS X airport command result parser',
    author='Egemen Yildiz',
    author_email='egemenyildiz.e@gmail.com',
    url='https://github.com/egemenyildiz/airport-py',
    packages=find_packages(),
    python_requires="<=2.7.15",
    classifiers=[
        'Programming Language :: Python :: 2 :: Only',
        'License :: OSI Approved :: MIT License',
        'Operating System :: MacOS :: MacOS X',
    ],
)

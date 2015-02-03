#!/usr/bin/env python
__author__ = 'Delhivery'

from distutils.core import setup
from setuptools import setup, find_packages

setup(
        name='SES_emails',
        version='0.1',
        description='App will help in maintaining the list of SES_emails blocked by ses to prevent further bounce SES_emails',
        author='Delhivery',
        author_email='aamir.hussain@delhivery.com',
        packages=find_packages(),
        install_requires =['djangorestframework',],
        )


#!/usr/bin/env python
__author__ = 'Delhivery'

from distutils.core import setup
from setuptools import setup, find_packages

setup(
        name='ses_emails',
        version='0.2.1',
        description='App will help in maintaining the list of ses_emails blocked by ses to prevent further bounce ses_emails',
        author='Delhivery',
        author_email='aamir.hussain@delhivery.com',
        packages=find_packages(),
        install_requires=['djangorestframework',],
        )


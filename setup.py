#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from setuptools import setup, find_packages

VERSION = '1.0.3'

setup(
    name='django-adminrestrict-CDSP',
    version=VERSION,
    description="Django admin restriction",
    long_description=open("README.md").read(),
    keywords='authentication, django, security',
    author='Alexandre Chevallier (fork) Robert Romano (original author)',
    author_email='alexandre.chevallier@sciencespo.fr',
    url='https://github.com/AChevallier/django-adminrestrict',
    license='MIT',
    package_dir={'adminrestrict-CDSP': 'adminrestrict-CDSP'},
    include_package_data=True,
    packages=find_packages(),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: Log Analysis',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Middleware',
        'Topic :: Security',
        'Topic :: System :: Logging',
    ],
    zip_safe=False,
)

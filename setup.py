#!/usr/bin/env python

import setuptools
from distutils.core import setup

setup(name='wimiko',
	version='1.3.2',
	description='Secure Transport Protocol in Python',
	long_description="""
    Wimiko provides an encrypted connection between a chosen host and you
	""",
	author='Rayan Haddad',
	author_email='rayan.m.@icloud.com',
	url='https://github.com/Rayan25062011/wimiko',
    readme = 'README.md',
	packages=[
			'wimiko.py'
		],
	scripts = [
			'wimiko.py'
		],
	install_requires=[
			'ssl',
          	'urllib',
          	'urllib3',
          	'sys',
          	'os'
	  	],
)

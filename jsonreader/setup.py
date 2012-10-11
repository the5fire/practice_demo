#coding:utf-8
#!/usr/bin/env python

from setuptools import setup, find_packages


setup(
    name = 'jsonreader',
    version = '0.0.1',
    description = 'a json reader base on wxpython',
    author = 'the5fire',
    author_email = 'thefivefire@gmail.com',
    url = 'http://www.the5fire.net',
    packages = find_packages(),
    install_requires = [
    ],
    entry_points = {
        'console_scripts': [
            'jsonreader = jsonreader.jsonreader:main'    
        ]    
    }
)

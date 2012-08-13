#coding:utf-8
'''

'''
import os
import sys

from setuptools import setup, find_packages


setup(
    name = "djangodemo",
    version = "0.0.1",
    packages = find_packages(exclude=["demo/*"]),
    
    include_package_data = True, 
    
    install_requires = [
        'django>=1.3'
    ],
    
    entry_points = {
        'console_scripts' : [
            'djangodemo = djangodemo.server:run'
        ],
    },
    author = "the5fire",
    author_email = 'myemail@email.com',
    url = "http://www.the5fire.net",
    description = 'a demo for setuptools',
)

#!/usr/bin/env python
#-*- coding:utf-8 -*-

#############################################
# File Name: setup.py
# Author: xingming
# Mail: huoxingming@gmail.com
# Created Time:  2015-12-11 01:25:34 AM
#############################################


from setuptools import setup, find_packages

setup(
    name = "bsn_sdk_py",
    version = "1.0.0",
    keywords = ("bsn","blockchain", "Beijing Red Date", "bsn_sdk_py"),
    description = "bsn sdk",
    long_description = "bsn sdk 2020/04/23",
    license = "MIT Licence",

    url = "https://github.com/helailiang/bsn-sdk-python",
    author = "helailiang",
    author_email = "helailiang@reddatetech.com",

    packages = find_packages(),
    include_package_data = True,
    platforms = "any",
    install_requires = ['hkdf==0.0.3','cryptography==2.7','fabric-sdk-py==0.8.1']
)
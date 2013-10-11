#!/usr/bin/env python
from distutils.core import setup

setup(
    name='genpass',
    py_modules=['genpass'],
    author='ChangZhuo Chen',
    version='0.0.1',
    license='MIT',
    description='Generate Password',
    long_description=open('README.md').read(),
    scripts=['bin/genpass'],
    url='https://github.com/czchen/genpass',
    install_requires=[
        'pbkdf2',
        'xerox',
    ],
)

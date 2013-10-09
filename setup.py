#!/usr/bin/env python
from distutils.core import setup

setup(
    name='GenPass',
    author='ChangZhuo Chen',
    version='0.0.1',
    license='MIT',
    description='Generate Password',
    long_description=open('README.md').read(),
    scripts=['bin/gen_pass.py'],
    url='https://github.com/czchen/gen_pass',
    install_requires=[
        pbkdf2==1.3,
    ],
)

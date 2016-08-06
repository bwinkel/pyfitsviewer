#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup


setup(
    name='pyfitsviewer',
    version='0.1.0',
    author='Sven Brauch',
    author_email='mail@svenbrauch.de',
    description=(
        'pyfitsviewer: a GUI to inspect FITS files, similar to fv'
        ),
    scripts=['pyfv'],
    install_requires=[
        'setuptools',
        'numpy>=1.8',
        'matplotlib>=1.4',
        'astropy>=1.0',
    ],
    packages=['pyfitsviewer'],
    package_dir={
        'pyfitsviewer': 'src',
        },
    package_data={
        'pyfitsviewer': ['forms/*.ui']
        },
    # url='https://github.com/scummos/pyfitsviewer/',
    # download_url='https://github.com/scummos/pyfitsviewer/tarball/0.1.0',
    # keywords=['astronomy']
)

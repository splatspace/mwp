#!/usr/bin/env python
# -*- coding: utf-8 -*-
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

requirements = [
    'Jinja2',
    'python-wordpress-xmlrpc',
    'requests'
]

setup(
    name='mwp',
    version='0.1.0',
    description='Post your meetup calendar to wordpress.',
    long_description=readme + '\n\n' + history,
    author='j.c.sackett',
    author_email='jcsackett@splatspace.org',
    url='https://github.com/splatspace/mwp',
    packages=[
        'mwp',
    ],
    package_dir={'mwp':
                 'mwp'},
    include_package_data=True,
    install_requires=requirements,
    license="BSD",
    zip_safe=False,
    keywords='mwp',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ],
    entry_points="""\
    [console_scripts]
    mwp = mwp.mwp:main
    """
)

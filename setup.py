#!/usr/bin/env python

from distutils.core import setup

setup(
    name='pytest-reportinfra',
    packages=['pytest-reportinfra'],
    version='0.1',
    description='Pytest plugin for reportinfra',
    author='Thomas Liske',
    author_email='thomas@fiasko-nw.net',
    url='https://github.com/liske/python-pytest-reportinfra',
    download_url='https://github.com/liske/python-pytest-reportinfra/archive/0.1.tar.gz',
    keywords=['pytest', 'py.test', 'reportinfra'],
    install_requires=['pytest', 'testinfra'],
    license='GPLv3+',
    long_description=open('README.md', 'r').read(),
    long_description_content_type='text/markdown',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Plugins',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Framework :: Pytest',
    ],
)

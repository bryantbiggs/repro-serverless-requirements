#!/usr/bin/env python
"""
    Setup
    -----

    Enables the `setuptools` to build and install the library

"""

from setuptools import setup, find_packages

packages = ['sdk']

requires = [
    'boto3~=1.9.2',
    'botocore~=1.12.2',
    'requests~=2.19.1'
]
test_requirements = [
    'pytest~=3.5.0',
    'pytest-cov'
]


try:
    import pypandoc
    description = pypandoc.convert('README.md', 'rst')
except (IOError, ImportError):
    description = ''

setup(
    name='sdk',
    version='0.1.0',
    description='Internal software development kit',
    long_description=description,
    long_description_content_type='text/markdown',
    author='Bryant Biggs',
    author_email='youremail@youraddress.com',
    packages=find_packages(),
    package_dir={'sdk': 'sdk'},
    python_requires=">=3.6",
    install_requires=requires,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Topic :: Software Development :: Libraries',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6'
    ],
    tests_require=test_requirements
)

#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages


def get_version(filename):
    """Extract the package version"""
    with open(filename) as in_fh:
        for line in in_fh:
            if line.startswith('__version__'):
                return line.split('=')[1].strip()[1:-1]
    raise ValueError("Cannot extract version from %s" % filename)


with open('README.rst') as readme_file:
    readme = readme_file.read()

try:
    with open('HISTORY.rst') as history_file:
        history = history_file.read()
except OSError:
    history = ''

requirements = ['sympy', 'qnet==2.0.0-dev', 'trajectorydata']

dev_requirements = [
    'coverage', 'pytest', 'pytest-cov', 'pytest-xdist', 'twine', 'pep8',
    'flake8', 'wheel', 'sphinx', 'sphinx-autobuild', 'sphinx_rtd_theme']
dev_requirements.append('better-apidoc')


version = get_version('./src/qnet_qsd/__init__.py')

setup(
    author="Michael Goerz",
    author_email='mail@michaelgoerz.net',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    description="A code-converter and simulation driver between QNET and QSD",
    dependency_links=[
        'git+https://github.com/mabuchilab/QNET.git@develop#egg=QNET-2.0.0-dev'
    ],
    install_requires=requirements,
    extras_require={
        'dev': dev_requirements,
    },
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='qnet_qsd',
    name='qnet_qsd',
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    url='https://github.com/mabuchilab/qnet_qsd',
    version=version,
    zip_safe=False,
)

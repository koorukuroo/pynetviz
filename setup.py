# -*- coding: utf-8 -*-

import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='pynetviz',
    version='0.1',
    description='Python Network(Graph) Visualization',
    author='Kyunghoon Kim',
    author_email='kyunghoon@unist.ac.kr',

    license = "MIT License",
    keywords = ['Network', 'Graph', 'Visualization'],
    url = "https://github.com/koorukuroo/pynetviz",
    packages=[
        'pynetviz',
        ],
    install_requires=['networkx'],
    long_description=read('README.rst'),
    classifiers=[
        "Programming Language :: Python",
        "License :: OSI Approved :: MIT License",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Scientific/Engineering :: Visualization",
    ],
)

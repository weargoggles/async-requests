from setuptools import setup
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='requests-async',

    version='0.0.1',

    description='asyncio wrapper for Requests',
    long_description=long_description,

    license='MIT',

    install_requires=[
        'requests'
    ],
    packages=['requests_async'],
)

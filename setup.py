from setuptools import setup, find_packages

from nnlp import __version__

setup(
    name='nnlp',
    version=__version__,
    description='A python package for the development of college students.',

    url='https://github.com/Avirup-R/Ninja_hattori',
    author='Aditya and Avirup',
    author_email='avirakshit2002@gmail.com',

    packages=find_packages(),

    classifiers=[
        'Intended Audience :: Developers',

        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
    ],
)

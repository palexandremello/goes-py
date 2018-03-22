# -*- coding: utf-8 -*-
from setuptools import setup
setup(
    name='goespy',
    version='0.1.1',
    url='https://github.com/palexandremello/goes-py',
    license='BSD 2-Clause License',
    author='Paulo Alexandre Mello',
    author_email='palexandremello@gmail.com',
    keywords='weather goes satellite meteorology noaa',
    description=u'A Python package can be useful to download dataset from goes satellite on AWS',
    packages=['goespy'],
    install_requires=['boto3','botocore','pathlib'],
    zip_safe=False)


import ez_setup
ez_setup.use_setuptools()
from setuptools import setup

setup(
    name='modis',
    version='0.3.0',
    packages=['modis'],
    install_requires=[
      'requests',
      'xmltodict'
  ],
    py_modules=['modis'],
)

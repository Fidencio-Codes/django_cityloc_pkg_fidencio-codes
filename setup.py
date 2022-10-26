from setuptools import setup, find_packages 

# put the contents of your README file into the long_description
from pathlib import Path 
this_directory = Path(__file__).parent
long_description = (this_directory / "README.rst").read_text()

setup(
    long_description=long_description)


### The setup.py is the installation entry point used to install your new package, 
# generate distribution files, and more. The details provided here will be used in 
# the PKG-INFO file that will be generated which will contain metadata about your package.
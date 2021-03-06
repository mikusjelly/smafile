import os

from setuptools import find_packages, setup
from smafile import __VERSION__


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="smafile",
    version=__VERSION__,
    author="mikusjelly",
    author_email="mikusjelly@gmail.com",
    description=("parse smali file"),
    license="MIT",
    keywords="smali",
    url="https://github.com/mikusjelly/smafile",
    packages=find_packages(exclude=['tests']),

    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Utilities",
    ]
)

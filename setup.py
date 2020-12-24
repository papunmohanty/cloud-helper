import pathlib
from sys import path
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="cloud-helper",
    version="1.0.0",
    description="A convenient Helper library for various cloud services",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/papunmohanty/cloud-helper",
    author="Papun Mohanty",
    author_email="reachtopmohanty@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
    ],
    packages=["cloud_helper"],
    include_package_data=True,
    install_requires=["boto3"],
)

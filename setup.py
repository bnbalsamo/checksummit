from setuptools import setup, find_packages

def readme():
    with open("README.md", 'r') as f:
        return f.read()

setup(
    name = "checksummit",
    description = "A REST API Microservice for computing checksums",
    long_description = readme(),
    packages = find_packages(
        exclude = [
        ]
    ),
    install_requires = [
        'flask>0',
        'flask_restful',
        'nothashes'
    ],
    dependency_links = [
        'https://github.com/bnbalsamo/nothashes' +
        '/tarball/master#egg=nothashes'
    ]
)

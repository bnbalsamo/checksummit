from setuptools import setup, find_packages


def readme():
    with open("README.md", 'r') as f:
        return f.read()


setup(
    name="checksummit",
    description="An API for computing checksums and hashes",
    version="0.2.2",
    long_description=readme(),
    author="Brian Balsamo",
    author_email="brian@brianbalsamo.com",
    packages=find_packages(
        exclude=[
        ]
    ),
    include_package_data=True,
    url='https://github.com/bnbalsamo/checksummit',
    install_requires=[
        'flask>0',
        'flask_env',
        'flask_restful',
        'multihash',
        'nothashes'
    ],
    tests_require=[
        'pytest'
    ],
    test_suite='tests'
)

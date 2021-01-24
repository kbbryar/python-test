from setuptools import setup, find_packages

setup(
    name='simpleclass',
    version="1.0",
    author="Ken Bryar",
    description="This is a simple class to test the setup script.",
    url="https://github.com/kbbryar/python-test.git",
    packages=find_packages(),
    tests_require=["pytest"],
)

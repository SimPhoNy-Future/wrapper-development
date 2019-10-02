from setuptools import setup, find_packages

from packageinfo import VERSION, NAME

# Read description
with open('README.rst', 'r') as readme:
    README_TEXT = readme.read()


# main setup configuration class
setup(
    name=NAME,
    version=VERSION,
    author='Author info',
    url='www.some_website.some_domain',
    description='The wrapper of something for SimPhoNy',
    keywords='simphony, cuds, something',
    long_description=README_TEXT,
    install_requires=[
        'simphony>=3.0.0',
        'unittest2',
    ],
    packages=find_packages(),
    test_suite='wrapper.testing',
    entry_points={
        'wrappers':
            'wrapper = wrapper.wrapper_session:WrapperSession'},
)
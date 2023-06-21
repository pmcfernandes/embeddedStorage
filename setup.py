from setuptools import setup


def readme():
    with open('README.md') as f:
        return f.read()


setup(
    name='embeddedStorage',
    version='1.0.1',
    description='Lib Key/value pair database in embedded systems like raspberry pi',
    long_description=readme(),
    author='Pedro Fernandes',
    url='https://github.com/pmcfernandes/embeddedStorage',
    packages=[
        ''
    ],
    license='GPLv3+'
)
from setuptools import setup

setup(
    name='fxrt',
    version='1.0',
    description='Realtime FX prices',
    author='Philippe Remy',
    license='MIT',
    long_description_content_type='text/markdown',
    long_description=open('README.md').read(),
    packages=['fxrt'],
    install_requires=[
        'requests'
    ]
)

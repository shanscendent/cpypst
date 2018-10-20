from setuptools import setup

setup(
    name = 'cpypst',
    version = '0.0.1',
    packages = ['cpypst'],
    entry_points = {
        'console_scripts': [
            'cpypst = cpypst.__main__:main'
        ]
    })
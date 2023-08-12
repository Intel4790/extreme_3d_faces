from setuptools import setup, find_packages

setup(
    name='app',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        line.strip() for line in open('requirements.txt')
    ],
    entry_points={
        'console_scripts': [
            'app=src.main:main',
        ],
    },
)
import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst'), encoding='utf-8') as readme:
    README = readme.read()

setup(
    name='getvimrc',
    version='0.0.1',
    packages=find_packages(exclude=('tests',)),
    include_package_data=True,
    license='MIT License',
    description='Get vimrc and dein settings(python)',
    long_description=README,
    url='https://github.com/naritotakizawa/getvimrc',
    author='Narito Takizawa',
    author_email='toritoritorina@gmail.com',
    classifiers=[
        "Environment :: Console",
        'Programming Language :: Python',
        "Programming Language :: Python :: 3",
    ],
    entry_points={'console_scripts': [
        'getvimrc = getvimrc.__main__:main'
    ]},
)

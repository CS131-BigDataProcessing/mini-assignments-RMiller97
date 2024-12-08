from setuptools import setup, find_packages

setup(
    name='crime_test',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
       'iniconfig==2.0.0',
       'numpy==2.1.3',
       'packaging==24.2', 
       'pandas==2.2.3',
       'pluggy==1.5.0',
       'pytest==8.3.4',
       'python-dateutil==2.9.0.post0',
       'pytz==2024.2',
       'six==1.17.0',
       'tzdata==2024.2',
    ],
    author='Ryan Miller',
    description='A package to validate crime data'
)

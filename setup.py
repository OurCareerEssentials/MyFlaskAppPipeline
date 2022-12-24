from setuptools import find_packages
from setuptools import setup

setup(
    name='Python-flaskapp',
    version='1.0.0',
    description='Flask app',
    author='Flask author',
    install_requires=[],   
    keywords='sample, setuptools, development',
    packages=find_packages(where='src'),
    extras_require={  
        'dev': ['check-manifest'],
        'test': ['coverage'],
    },
    project_urls={  
        'Bug Reports': 'https://github.com/RevanthTiruveedhi/PythonFlaskApp.git',
    }
)
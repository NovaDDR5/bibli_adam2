from setuptools import *

setup(
    name='bibli_adam_64bit_html',
    version='0.0.4',
    description="tentative de creation d'une librairie d'encodage 64bit et HTML utilisable avec pip",
    license='MIT',
    packages=find_packages(where="src"),
    package_dir={'': 'src'},
    author='NovaDDR5',
    author_email='cd_rwx@gmail.com',
    keywords=['example'],
    url='https://github.com/NovaDDR5/bibli_adam2'
)
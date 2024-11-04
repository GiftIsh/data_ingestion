from setuptools import setup, find_packages

setup(
    name='data_ingestion',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='EDSA project python package',
    long_description=open('README.md').read(),
    install_requires=['pandas', 'sqlalchemy'],
    url='https://github.com/<username>/<package-name>',
    author='Gift Ishimwe',
    author_email='ishimwegift.02@gmail.com'
)
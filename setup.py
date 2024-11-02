from setuptools import setup, find_packages

setup(
    name= 'data_ingestion' , 
    version= '0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='EDSA example python package',
    long_description=open('readme.MD').read(),
    install_requires=['numpy'],
    url='https://github.com/Satota20/Satota20',
    author='<Omar Setait>',
    author_email='<setait88@gmail.com>'
)
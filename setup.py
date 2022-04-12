# this will call the setuptools modules and import the setup and find_packages functions from it

from setuptools import setup, find_packages

#This will read the package description from our README.rst file
with open('README.rst', encoding='UTF-8') as f:
    readme = f.read()

# This will do the calling out to setup and set some of the information about the package itself
setup(
    name='hr',
    version='1.0.0',
    description='command line user export utility',
    author='Efe Erike',
    author_email='efe.erike@gmail.com',
    #This will define where to look for packages itself. We are pointing to the src directory
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=[],
    
    # This is essentially saying:
    # When you are installed, create an executable named hr,
    # that will call the "main" method inside the "cli" module,
    # inside of the "hr" package.
    entry_points={
        'console_scripts': 'hr=hr.cli:main',
    }

)

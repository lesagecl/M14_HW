from setuptools import setup, find_packages

setup(
    name='BookLoverPackage',
    version='1.0.0',
    url='https://github.com/lesagecl/M14_HW',
    author='Chelsea Le Sage',
    author_email='cl5bd@virginia.edu',
    description='book lover package',
    packages=find_packages(),    
    install_requires=['numpy >= 1.11.1', 'matplotlib >= 1.5.1'],
)


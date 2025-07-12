from setuptools import setup, find_packages
from typing import List



# Function to get requirements from a file


def get_requirements(file_path:str) -> List[str]:

    """
    This function reads a requirements file and returns a list of requirements.
    :param file_path: Path to the requirements file
    :return: List of requirements
    """
    requirements=[]
    with open(file_path) as file:
        requirements = file.readlines()
        requirements = [req.replace("\n","") for req in requirements]

        if '-e .' in requirements:
            requirements.remove('-e .')
    return requirements




#setup.py 


setup(
    name='my_package',
    version='0.1.0',
    description='A sample Python package',
    author='Joydip Rakshit',
    packages=find_packages(),
    install_requires=get_requirements('requirement.txt'),
)
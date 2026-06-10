from setuptools import find_packages,setup
from typing import List 

HYPEN_E_DOT = "-e ."

def get_requirements(file_path='requirements.txt'):
    '''
    This function will return the list of requirements 
    '''
    requirements = []
    with open(file_path) as file_ojc:
        requirements = file_ojc.readlines()
        requirements = [req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

        return requirements
setup(

    name = "mlproject",
    version = "0.0.1",
    author = "bejuka",
    author_email = "bcapbitest@gmail.com",
    packages = find_packages(),
    install_requires = get_requirements('requirements.txt')

)
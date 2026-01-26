from setuptools import find_packages, setup
from typing import List

def get_requirements(filepath:str)->List[str]: 
    ''' 
    This function return a list of requirements
    '''
    requirements = []

    with open(filepath) as file: 
        for library in file.readlines(): 
            requirements.append(library.replace("\n", ""))

    if "-e ." in requirements: 
        requirements.remove("-e .")

    return requirements


setup(
    name ='mlproject', 
    version = '0.0.1', 
    author = "Deepak",
    author_email='deepakkrishna2206@gmail.com', 
    packages=find_packages(), 
    install_requires=get_requirements('requirements.txt')
)
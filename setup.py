from setuptools import setup, find_packages
from typing import List 

HYPEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> list:
    '''This function will return the list of requirements'''
    requirements = []
    with open(file_path) as file:
        for line in file.readlines():
            requirements.append(line.strip())
            if HYPEN_E_DOT in requirements:
                requirements.remove(HYPEN_E_DOT)
    return requirements
setup(
    name="mlproject",
    version="0.1",
    author="Achuth Abhay",
    author_email="achuthabhay0@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")
)
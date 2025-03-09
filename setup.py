#why we do this is , with help of setup we can build our entire project in form of packages  any one can use it 
from setuptools import setup,find_packages
from typing import List
HYPEN_E_DOT='-e .'

def get_requirements(file_path:str)->List[str]:
    #this will return list of requiremnts 
    requirements=[]
    with open(file_path) as file:
        requirements=file.readlines()
        requirements=[req.replace('\n','') for req in requirements]
        if HYPEN_E_DOT in requirements:
           requirements.remove(HYPEN_E_DOT)


setup(
    name="mlproject",
    version='0.0.1',
    author='abhishek gl',
    author_email='abhishekgl1659655@gmail.com',
    packages=find_packages(),
    #install_requires=['pandas','numpy','seaborn'] so here its not possible to give each and every path like this so i will make a function .
    install_requires=get_requirements('requirements.txt')
)
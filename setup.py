from setuptools import find_packages,setup
from typing import List

Hyp_E='-e .'

def get_requirements(file_path:str)->List[str]:
    '''
    This function returns the list of environments
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace('\n','') for req in requirements]
        if Hyp_E in requirements:
            requirements.remove(Hyp_E)    
    return requirements
setup(
name='mlproject',
version='0.0.1',
author="Aditi",
author_email='aditichapagain05@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')
)
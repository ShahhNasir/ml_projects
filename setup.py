from setuptools import find_packages,setup
from typing import List


HYPEN_E_DOT = '-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    This Function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[require.replace("\n","")for require in requirements]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements
    

setup(
    name = 'ML_project',
    version='0.0.1',
    Author='Nasir Hussain',
    install_requires=get_requirements('requirements.txt'),
    author_email='Shahhnasir83@gmail.com',
    packages=find_packages()
    


)
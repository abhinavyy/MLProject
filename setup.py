from setuptools import find_packages, setup # type: ignore
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    '''
    This function returns the list of requirements.
    '''
    requirements = []
    with open(file_path) as file_obj:
        # Read all lines instead of just one
        requirements = file_obj.readlines()
        # Strip whitespace and newline characters
        requirements = [req.strip() for req in requirements]

        # Remove '-e .' if present
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements

setup(
    name='MLProject',
    version='0.0.1',  # Corrected 'verion' to 'version'
    author='Abhinav',
    author_email='abhinavat3791@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)

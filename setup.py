#setup.py---To convert the source code into Library format so that it can be installed & imported /used in other files by pip install package_name & import package_name
from setuptools import find_packages,setup
from typing import List
REQUIREMENT_FILE_NAME=requirements.txt
def get_requirements()->List[str]:

    #List[str] returnds list of libraries from requirements.txt
    with open(REQUIREMENT_FILE_NAME) AS requirement_file:
        requirement_list=requirement_file.readlines()
    requirement_list=requirement_name.replace("\n","")for requirement_name in requirement_list
    if HYPHEN_E_DOT in requirement_list:
        requirement_list.remove(HYPHEN_E_DOT)
    return requirement_list



setup(
    name="sensor",
    version="0.0.1",
    author="vijayLalam",
    author_email="vijaysankar117@gmail.com",
    #find_packages() will try to search the folder(ex: sensor) having pytho code along with __init__.py and consider the folder(ex: Sensor) as package/Library and the python code file as Module
    packages=find_packages(),
    install_requires=get_requirements(),
)
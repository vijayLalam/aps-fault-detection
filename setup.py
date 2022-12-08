#setup.py---To convert the code into Library format so that it can be used in other files by pip install package_name & import package_name
from setuptools import find_packages,setup
def get_requirements():
    pass

setup(
    name="sensor",
    version="0.0.1",
    author="vijayLalam",
    author_email="vijaysankar117@gmail.com",
    #find_packages() will try to search the folder(ex: sensor) having pytho code along with __init__.py and convert the folder into package/Library and the python code file is Module
    packages=find_packages(),
    #
    install_requires=get_requirements(),
)
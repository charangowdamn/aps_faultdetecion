#setup.py file is used for the distribution of the files
from setuptools import find_packages,setup
from typing import List

REQUIREMENT_FILE_NAME = "requirements.txt"
HYPEN_E_DOT = "-e ."
def get_requirements():
    #provide the list of libraries
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        requirement_list = requirement_file.readlines()
        requirement_list = [requirementname.replace("\n","") for requirementname in requirement_list]
        if HYPEN_E_DOT in requirement_list:
            requirement_list.remove(HYPEN_E_DOT)
        return requirement_list   
    pass

setup(
    name = "sensor",
    version="0.0.1",
    author="charangowdamn",
    author_email="charangowda2k@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements(),
)


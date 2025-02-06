# configuration info about the project
from setuptools import find_packages,setup
from typing import List

# function to return list of requirements
def get_requirements()-> List[str]:
    requirement_lst:List[str] = []
    try:
        with open('requirements.txt', 'r') as file:
            lines = file.readlines()
            # Process each line
            for line in lines:
                requirement = line.strip()
                if requirement and requirement != '-e .':
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found")

    return requirement_lst

print(get_requirements())

# Setting up meta data
setup(
    name = "Network Security System",
    version = "0.0.1",
    author = "Jimmy",
    author_email = "jimmymuthoni26@gmail.com",
    packages = find_packages(),
    install_requires = get_requirements()
)
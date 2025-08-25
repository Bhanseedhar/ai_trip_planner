
from setuptools import setup, find_packages
from typing import List

def get_requirements() -> List[str]:
    
    requirements_list:List[str] =[]

    try:
        with open("requirements.txt") as file:
            lines = file.readlines()
            for line in lines:
                requirement=line.strip()# strips white space and next line char
                if requirement and requirement!='-e .':
                    requirements_list.append(requirement)

    except FileNotFoundError:
        print("requirements.txt File not found")

    return requirements_list
print(get_requirements())


setup(
    name="ai_trip_planner",
    version="0.1.0",
    description="An AI-powered trip planner.",
    author="Bhansee",
    packages=find_packages(),
    install_requires=get_requirements(),
    python_requires=">=3.7",
)
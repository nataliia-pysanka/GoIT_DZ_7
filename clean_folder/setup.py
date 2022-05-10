from setuptools import setup, find_namespace_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="clean_folder_superb",
    version="0.0.1",
    author="Nataliia Pysanka",
    author_email="pysankanataliia@gmail.com",
    description="Package to clean your folders",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/nataliia-pysanka/clean_folder_superb",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=find_namespace_packages(),
    entry_points={'console_scripts': [
        'clean_folder=clean_folder.main:main'
    ]}
)

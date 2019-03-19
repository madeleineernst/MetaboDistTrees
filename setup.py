import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="MetaboDistTrees",
    version="0.0.7",
    author="Madeleine Ernst",
    author_email="mernst@ucsd.edu",
    description="A python implementation for building chemically informed distance trees",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/madeleineernst/MetaboDistTrees",
    packages=setuptools.find_packages(),
    package_data={
        # If any package contains *.txt files, include them:
        '': ['*.txt'],
        # And include any *.dat files found in the 'data' subdirectory
        # of the 'mypkg' package, also:
        'MetaboDistTrees': ['data/*.obo'],
    },
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
    setup_requires=["pytest-runner"],
    tests_require=["pytest"],
)

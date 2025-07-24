from setuptools import setup
from setuptools import find_packages

# PEP0440 compatible formatted version, see:
# https://www.python.org/dev/peps/pep-0440/
# https://github.com/scikit-learn/scikit-learn/blob/sklearn/setup.py

#   X.Y.0   # For first release after an increment in Y
#   X.Y.Z   # For bugfix releases

# Dev branch marker is: 'X.Y.dev' or 'X.Y.devN' where N is an integer.
# 'X.Y.dev0' is the canonical version of 'X.Y.dev'

setup(
    name="FloodPredictions",
    version="0.1dev",
    packages=[
        "FloodPredictions",
    ],
    long_description=open("README.md").read(),
)
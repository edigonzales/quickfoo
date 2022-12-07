import os
from setuptools import setup, find_packages

# buildNumber = 'LOCALBUILD'
# if os.environ.get('GITHUB_RUN_NUMBER'): 
#     buildNumber = os.environ.get('GITHUB_RUN_NUMBER')
 
with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="quickfoo",                        # This is the name of the package
    version="0.0.6",                        # The initial release version
    author="Stefan Ziegler",                # Full name of the author
    description="QuickFoo Test Package",
    long_description=long_description,      # Long description read from the the readme file
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        'Operating System :: POSIX :: Linux',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: MacOS',
    ],                                      # Information to filter the project on PyPi website
    python_requires='>=3.8',                # Minimum version requirement of the package
    py_modules=["quickfoo"],                # Name of the python package
    packages=find_packages(where="src"),
    package_dir={'':'src'},        # Directory of the source code of the package
    package_data={'lib_ext':['*.h', '*.lib', '*.dll', '*.so', '*.dylib']},
    install_requires=['importlib-resources']                     # Install other dependencies if any
)

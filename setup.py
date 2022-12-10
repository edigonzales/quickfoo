import os
from setuptools import setup, find_packages

# buildNumber = 'LOCALBUILD'
# if os.environ.get('GITHUB_RUN_NUMBER'): 
#     buildNumber = os.environ.get('GITHUB_RUN_NUMBER')

with open('README.md') as readme_file:
    readme = readme_file.read()

setup(
    author="Stefan Ziegler",
    author_email='edi.gonzales@gmail.com',
    python_requires='>=3.8',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        'Operating System :: POSIX :: Linux',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: MacOS',
    ],
    description="Python Boilerplate contains all the boilerplate you need to create a Python package.",
    install_requires=['importlib-resources'] ,
    license="MIT license",
    long_description=readme,
    include_package_data=True,
    keywords='ilivalidator',
    name='quickfoo',
    packages=find_packages(include=['quickfoo', 'quickfoo.*']),
    package_data={'quickfoo.lib_ext':['*.h', '*.lib', '*.dll', '*.so', '*.dylib']},
    #test_suite='tests',
    #tests_require=test_requirements,
    url='https://github.com/edigonzales/ilivalidator_python',
    version='0.0.6',
    zip_safe=False,
)

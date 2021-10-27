from setuptools import setup, find_packages

VERSION = '0.0.7'
DESCRIPTION = 'Python DICOM image manipulator'
LONG_DESCRIPTION = 'Python DICOM image Manipulator allows for direct manipulation of DICOM images in python'

# Setting up
setup(
       # the name must match the folder name 'verysimplemodule'
        name="pydicomimg",
        version=VERSION,
        author="Ryan Hennessey",
        author_email="<ryanphennessey@gmail.com>",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=['pydicom','numpy'], # add any additional packages that
        # needs to be installed along with your package. Eg: 'caer'

        keywords=['python', 'DICOM', 'Image', 'resize', 'rotate', 'flip'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)

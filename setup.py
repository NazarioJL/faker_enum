#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import io

from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))
README = io.open(os.path.join(here, "README.rst"), encoding="utf8").read()

version = "0.0.2"

try:
    import pkgutil
    import zipimport

    zip_safe = (
        hasattr(zipimport.zipimporter, "iter_modules")
        or zipimport.zipimporter in pkgutil.iter_importer_modules.registry.keys()
    )
except (ImportError, AttributeError):
    zip_safe = False

setup(
    name="faker_enum",
    version=version,
    description="Enum provider for the Faker Python package.",
    long_description=README,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Testing",
        "Topic :: Utilities",
    ],
    keywords="faker enum test data",
    author="NazarioJL",
    author_email="jlnazario@hotmail.com",
    url="https://github.com/NazarioJL/faker_enum",
    license="MIT License",
    package_dir={"faker_enum": "src/enum"},
    packages=["faker_enum"],
    platforms=["any"],
    test_suite="pytest",
    zip_safe=zip_safe,
    setup_requires=["pytest-runner"],
    tests_require=["pytest", "pytest-cov", "pytest-flakes", "pytest-pep8"],
    install_requires=["faker"],
)

from setuptools import find_packages, setup

from Sap2000py import __version__

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="Sap2000py",
    version=__version__,
    description="Sap2000 API python interface",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Lingyun Gou",
    author_email="17717910647@163.com",
    url="https://github.com/ganansuan647/Sap2000py",
    license="GPL Licence",
    keywords="Sap2000 API python",
    python_requires=">=3.4.3",
    package_dir={"": "Sap2000py"},
    packages=find_packages("Sap2000py"),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers in Structural Engineering',
        "Programming Language :: Python :: 3",
        "Operating System :: Microsoft :: Windows"
    ],
    install_requires=[
        "numpy",
        "comtypes>=1.1.11",
        "loguru",
        "pathlib",
        "rich",
    ],
)
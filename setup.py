from setuptools import setup, find_packages


setup(
    name="pypackbasics",
    version="1.0",
    description="Python Packaging Basics: An educational template package",
    url="https://github.com/AlanPearl/pypackbasics",
    author="Alan Pearl",
    author_email="alanpearl@pitt.edu",
    license="MIT",
    python_requires=">=3.6",  # note: 3.6 is required for f-strings
    install_requires=[
        "matplotlib",
        "numpy>=1.18",
    ],
    packages=find_packages()
)

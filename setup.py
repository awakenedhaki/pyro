from setuptools import setup

setup(
    name="pyro",
    version="0.1.0",
    packages=[
        "pyro", 
        "model", 
        "scraper", 
        "parsers", 
        "persistence", 
        "exceptions"
    ],
    url="https://github.com/awakenedhaki/pyro",
    license="MIT License",
    author="awakenedhaki",
    author_email="",
    description="Command line interface for Rosalind Bioinformatics Stronghold Problems",
    python_requires=">=3",
    install_requires=[
        "requests",
        "beautifulsoup4",
        "click"
    ]
)

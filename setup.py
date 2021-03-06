from setuptools import setup

setup(
    name="pyro",
    version="0.1.0",
    packages=[
        "pyro"
        'jsons'
    ],
    url="https://github.com/awakenedhaki/pyro",
    license="MIT",
    author="awakenedhaki",
    author_email="",
    description="Command line interface for Rosalind Bioinformatics Stronghold Problems",
    python_requires=">=3",
    install_requires=[
        'click',
        'requests',
        'beautifulsoup4'
    ]
)

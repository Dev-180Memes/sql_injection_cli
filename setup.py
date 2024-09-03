# setup.py

from setuptools import setup, find_packages

setup(
    name="sql_injection_cli",
    version="0.1",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "requests",
        "beautifulsoup4",
    ],
    entry_points={
        "console_scripts": [
            "sql-injection-cli=sql_injection_cli.cli:main",
        ],
    },
)

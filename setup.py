import setuptools

from io import open
from os import path

import pathlib
# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pretty-junit",
    version="0.0.1",
    author="Dinesh RVL",
    author_email="dinesh.rvl90@gmail.com",
    entry_points={
    'console_scripts': [
        'pretty-junit=convert:generate_html',
    ]
	},
    description="Library that converts junit xml into smart HTML Reports",
    long_description="Library that converts junit xml into smart HTML Reports",
    long_description_content_type="text/markdown",
    url="https://github.com/yessify/prettyJunit",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="text_processing",
    version="0.1",
    description="Testing for models confirming to the scikit-learn api",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/EricSchles/text_processing",
    author="Eric Schles",
    author_email="ericschles@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    packages=['text_processing',
              'text_processing.normalization',
              'text_processing.matching',
              'text_processing.parsing'
    ],
    include_package_data=True,
    install_requires=["spacy", "nltk", "pyspellchecker"],
)

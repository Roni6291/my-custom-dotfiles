from setuptools import find_packages, setup

# Load the README file.
with open(file="README.md") as readme_handle:
    long_description = readme_handle.read()

setup(
    # Define the library name, this is what is used along with `pip install`.
    name="house_price",
    # Define the author of the repository.
    author="Roni Abraham",
    # Define the Author's email, so people know who to reach out to.
    author_email="roni.abraham@tigeranalytics.com",
    # Define the version of this library.
    # Read this as
    #   - MAJOR VERSION 0
    #   - MINOR VERSION 1
    #   - MAINTENANCE VERSION 0
    version="0.3.0",
    # Here is a small description of the library. This appears
    # when someone searches for the library on https://pypi.org/search.
    description="A python client library used to predict median price of houses",
    # I have a long description but that will just be my README
    # file, note the variable up above where I read the file.
    long_description=long_description,
    # This will specify that the long description is MARKDOWN.
    long_description_content_type="text/markdown",
    # Here is the URL where you can find the code, in this case on GitHub.
    url="https://github.com/roniabrahamTA/House-Price-Prediction",
    # These are the dependencies the library needs in order to run.
    install_requires=[
        "pandas",
        "numpy",
        "six",
        "scipy",
        "scikit-learn",
    ],
    extras_require={
        "dev": [
            "pytest>=6.0",
            "pytest-cov>=2.0",
            "mypy>=0.931",
            "black>=22.1.0",
            "flake8>=4.0",
            "isort>=5.10.1",
            "tox>=3.24",
            "pre-commit>=2.17.0",
        ]
    },
    # test_suite="tests.run_my_test_suite",
    # Here are the keywords of my library.
    keywords="house price, median house price, real estate",
    # here are the packages I want "build."
    packages=find_packages(include=["house_price", "house_price.*"]),
    # # here we specify any package data.
    package_data={
        # include any files found subdirectory of the "extras", "training" package.
        "house_price.extras": ["log_cfg.json"],
        "house_price.training": ["*.json"],
    },
    # I also have some package data, like photos and JSON files, so
    # I want to include those as well.
    include_package_data=True,
    entry_points={
        "console_scripts": [
            "hpingest=house_price.ingestion:main_ingest",
        ]
    },
    scripts=["bin/hptrain.py", "bin/hpscore.py"],
    # Here I can specify the python version necessary to run this library.
    python_requires=">=3.7",
    # Additional classifiers that give some characteristics about the package.
    # For a complete list go to https://pypi.org/classifiers/.
    classifiers=[
        # I can say what phase of development my library is in.
        "Development Status :: Pre Release",
        # Here I'll add the audience this library is intended for.
        "Intended Audience :: Developers",
        "Intended Audience :: Data Science",
        "Intended Audience :: Real Estate",
        # Here I'll define the license that guides my library.
        "License :: OSI Approved :: MIT License",
        # Here I'll note that package was written in English.
        "Natural Language :: English",
        # Here I'll note that any operating system can use it.
        "Operating System :: OS Independent",
        # Here I'll specify the version of Python it uses.
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        # Here are the topics that my library covers.
        "Topic :: Real Estate",
        "Topic :: Education",
        "Topic :: Office/Business",
    ],
)

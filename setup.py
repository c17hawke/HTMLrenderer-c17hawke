import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

__version__ = "0.1.0"

## edit below variables as per your requirements -
REPO_NAME = "HTMLrenderer-c17hawke" # github repo name
AUTHOR_USER_NAME = "c17hawke" # update as per your need
SRC_REPO = "HTMLrenderer" # example sklearn etc
LIST_OF_REQUIREMENTS = [
        'ipython',
        'ipywidgets'
    ] # core dependencies

setuptools.setup(
    name="HTMLrenderer",
    version=__version__,
    author="c17hawke",
    author_email="sunny.c17hawke@gmail.com",
    description="A small package for rendering HTML pages in jupyter notebooks",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src", exclude="tests"),
    python_requires=">=3.6",
    install_requires=LIST_OF_REQUIREMENTS
)

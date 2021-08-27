import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="HTMLrenderer",
    version="0.0.7",
    author="c17hawke",
    author_email="sunny.c17hawke@gmail.com",
    description="A small package for rendering HTML pages in jupyter notebooks",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/c17hawke/HTMLrenderer-c17hawke",
    project_urls={
        "Bug Tracker": "https://github.com/c17hawke/HTMLrenderer-c17hawke/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
    install_requires=[
        'ipython',
    ],
)

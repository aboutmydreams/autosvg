import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="autosvg",
    version="0.0.1",
    author="aboutmydreams",
    author_email="aboutmydreams@163.com",
    description="Use a cool way to generate a svg file",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="your_github_url",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache License",
        "Operating System :: OS Independent",
    ],
)

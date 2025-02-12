from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="best_hashtags",
    version="0.1.1",
    author="Your Name",
    author_email="your.email@example.com",
    description="A tool to find the best hashtags for a given word",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/robertobalestri/best_hashtags",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        "requests",
        "beautifulsoup4",
    ],
)
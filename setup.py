from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="davis_summary_vac",
    version="0.1.0",
    author="Niranjan Gopalan",
    author_email="niranjangopalan948@gmail.com",
    description="A package for analyzing CSV files and generating summary reports in HTML",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Wearevac/davis-summary",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
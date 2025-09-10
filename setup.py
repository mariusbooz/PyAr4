from setuptools import setup, find_packages

setup(
    name="pyar4",
    version="0.1.0",
    author="",
    author_email="",
    description="A library to controll the Ar4-mk3 robotic arm.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    install_requires=[  # Dependencies
        # "requests>=2.20.0",
    ],
)

from setuptools import setup, find_packages

with open("requirements/prod.txt") as install_requires_file:
    requirements = install_requires_file.read().strip().split("\n")

setup(
    name="dataflowops",
    description="Testing modules for Prefect flows",
    license="Private",
    author="Kiwi Property",
    author_email="shruti.pulinkala@kp.co.nz",
    keywords="prefect",
    long_description_content_type="text/markdown",
    version="1.0",
    packages=find_packages(exclude=["tests"]),
    python_requires=">=3.9",
    install_requires=requirements,
    classifiers=[
        "Natural Language :: English",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Software Development :: Libraries",
    ],
)

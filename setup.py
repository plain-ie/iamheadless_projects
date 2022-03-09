from distutils.core import setup

setup(
    # Application name:
    name="iamheadless_projects",

    # Version number (initial):
    version="1.0.0",

    # Application author details:
    author="Maris Erts",
    author_email="maris@plain.ie",

    # Packages
    packages=["iamheadless_projects"],

    # Include additional files into the package
    include_package_data=True,

    # Details
    url="#",

    #
    license="LICENSE",
    description="#",

    # long_description=open("README.md").read(),

    # Dependent packages (distributions)
    install_requires=[
        "Django==4.0.1",
        "djantic==0.4.1",
        "networkx==2.6.3",
        "pydantic==1.9.0",
    ],
)

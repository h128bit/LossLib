from setuptools import setup, find_packages


setup(
    name="LossLib",
    version="1.0.1",
    author="h128bit",
    url="https://github.com/h128bit/LossLib",
    packages=find_packages(),
    install_requires=["torch"],
    project_urls={"GitHub": "https://github.com/h128bit/LossLib"},
    python_requires=">=3.10"
)

from setuptools import setup, find_packages

setup(
    name="task-tracker",
    version="1.0",
    packages=find_packages(),
    py_modules=["main"],
    install_requires=[
        "click",
    ],
    entry_points={
        "console_scripts": [
            "task=main:main",
        ],
    },
)

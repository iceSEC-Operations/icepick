from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="icepick",
    version="1.0.0",
    author="iceSEC",
    author_email="icesec@atomicmail.io",
    description="Advanced Penetration Suite — Precision strikes. Every time.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/iceSEC-Operations/icepick",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    entry_points={
        "console_scripts": [
            "icepick=icepick.cli:main",
        ],
        "gui_scripts": [
            "icepick-gui=icepick.cli:main",
        ],
    },
)
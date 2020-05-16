#! /usr/bin/env python3
# coding: utf-8
#
# author: kaku
# date: 2020/05/16
#
# GitHub:
#
#   https://github.com/kakukosaku
#
# Description:
#
from setuptools import find_namespace_packages, setup

setup(
    name="designpattern",
    version="0.1.1",
    packages=find_namespace_packages(where="src/main/python"),
    package_dir={
        "": "src/main/python"
    },
    install_requires=[
        #    "tornado>=4.0",
    ],
    dependency_links= [
        # "git+https://github.com/tqdm/tqdm.git@master#egg=tqdm",
    ],
    # 如果指定此项为True, 下面关于package data的定义无用
    # 必须有MANIFEST.in中指定项(不)需包含的文件
    # include_package_data=True,
    package_data={
        # If any package contains *.txt or *.rst files, include them:
        "": ["*.txt", "*.rst"],
        # And include any *.msg files found in the "hello" package, too:
        "config": ["*.yaml"],
    },
    exclude_package_data={
        "": ["*.mp3", "*.log"]
    },
    entry_points={
        "console_scripts": [
            "designPatternSayHi=design_pattern.greet:greet"
        ]
    },

    # metadata for upload to PyPI
    author="kaku",
    author_email="scugjs@gmail.com",
    description="Design Pattern python example implementation",
    license="PSF",
    keywords="design pattern",
    url="https://github.com/kakukosaku",   # project home page, if any
    project_urls={
        "pythonSkill": "https://github.com/kakukosaku/DesignPattern",
        "Documentation": "https://github.com/kakukosaku/pythonSkill",
        "Source Code": "https://github.com/kakukosaku/pythonSkill",
    }

    # could also include long_description, download_url, classifiers, etc.
)
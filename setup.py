#!/usr/bin/env python
# coding: utf-8

from distutils.core import setup

setup(
    name="ChinaWeather",
    version="0.1.0",
    description="实时获取城市的详细气象数据",
    author="numbbbbb",
    author_email="lj925184928@gmail.com",
    packages=["ChinaWeather", ],
    url="https://github.com/numbbbbb/ChinaWeather",
    license="WTFPL",
    install_requires=["beautifulsoup4>=4.3.2"],
    long_description=open("README.md").read(),
)

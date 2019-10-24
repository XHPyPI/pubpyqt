#!/bin/bash
# @Author: lamborghini1993
# @Date: 2019-09-30 11:06:05
# @UpdateDate: 2019-09-30 11:06:05
# @Description: 一键打包pypi并上传


python3 setup.py sdist bdist_wheel
python3 -m twine upload dist/*

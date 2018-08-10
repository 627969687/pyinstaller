#!/usr/bin/python
#coding=utf-8

import sys
import os

# 打包二进制路径转换
if getattr(sys, 'frozen', False):  # 运行于 |PyInstaller| 二进制环境
    basedir = sys._MEIPASS
else:  # 运行于一般Python 环境
    basedir = os.path.dirname(__file__)

DS = os.sep # 不同系统的斜杠识别
resDir = basedir + DS + 'res' + DS # 配置文件夹

class PyinstallerLearn(object):
	"""docstring for PyinstallerLearn"""
	def __init__(self):
		super(PyinstallerLearn, self).__init__()

	def main(self):
		print("main")

		with open(resDir+'test.txt') as file:
			print('读取文件内容: '+file.read())

		raw_input("输入任意字符退出: ")
		pass
		
PyinstallerLearn().main()
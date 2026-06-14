# -*- coding: utf-8 -*-

name = 'cmake'

version = '4.3.3'

tools = ['cmake', 'cpack', 'ctest']

build_requires = ['gcc', 'cmake']

variants = [['platform-linux', 'arch-x86_64', 'os-rocky-9.8', 'python-3.11+']]

def commands():
	env.PATH.append("{root}/bin")

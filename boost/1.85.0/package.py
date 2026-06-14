# -*- coding: utf-8 -*-

name = 'boost'

version = '1.85.0'

build_requires = ['gcc']

variants = [['platform-linux', 'arch-x86_64', 'os-rocky-9.8', 'python-3.11']]

build_command = """
cd {root} && \
{root}/bootstrap.sh --prefix={install_path} && \
{root}/b2 -q -d+2 --toolset=gcc release install && \
cd {build_path}
"""

def commands():
    appendenv('LD_LIBRARY_PATH', '{root}/lib/')
    appendenv('BOOST_ROOT', '{root}')



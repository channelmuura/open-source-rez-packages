# -*- coding: utf-8 -*-

name = 'tbb'

version = '2021.13.0'

variants = [['platform-linux', 'arch-x86_64']]

build_command = """
cp -r {root}/oneapi-tbb-2021.13.0/* {install_path}
"""

def commands():
    appendenv('LD_LIBRARY_PATH', '{root}/lib/intel64/gcc4.8')
    env.TBB_LOCATION.set('{root}')
    env.TBBROOT.set('{root}')
    env.TBB_LIBRARIES.set('{root}/lib/intel64/gcc4.8')
    env.TBB_INCLUDE_DIR.set('{root}/include')



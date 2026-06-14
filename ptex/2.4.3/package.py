# -*- coding: utf-8 -*-

name = 'ptex'

version = '2.4.3'

build_system = 'cmake'

def pre_build_commands():
    env.CXXFLAGS_STD.set("c++17")

@early()
def private_build_requires():
    import platform
    system = platform.system().lower()

    requires = ["cmake"]

    if system == 'linux':
        requires.append("gcc")
        
    return requires

@early()
def variants():
    from rez.package_py_utils import expand_requires
    
    # Resolves to platform, arch, and os packages
    requires = ["platform-**", "arch-**", "os-**"]

    return [expand_requires(*requires)]

def commands():
    appendenv('LD_LIBRARY_PATH', '{root}/lib64')
    setenv('PTEX_LOCATION', '{root}')


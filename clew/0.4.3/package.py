# -*- coding: utf-8 -*-

name = 'clew'

version = '0.4.3'

tools = ['clewTest']

private_build_requires = ['cmake']

@early()
def variants():
    from rez.package_py_utils import expand_requires
    
    # Resolves to platform, arch, and os packages
    requires = ["platform-**", "arch-**", "os-**"]

    return [expand_requires(*requires)]

def commands():
    env.LD_LIBRARY_PATH.append('{this.root}/lib')
    env.CLEW_INCLUDE_DIR.append('{this.root}/include')
    env.CLEW_LIBRARY.append('{this.root}/lib')
    env.CLEW_LOCATION.append('{this.root}')

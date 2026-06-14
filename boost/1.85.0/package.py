# -*- coding: utf-8 -*-

name = 'boost'

version = '1.85.0'

# Ensure you clean and setup again after each build if you have errors during build
build_command = """
cd {root} && \
{root}/bootstrap.sh --prefix={install_path} && \
{root}/b2 -q -d+2 --toolset=gcc release install && \
cd {build_path}
"""

@early()
def private_build_requires():
    import platform
    system = platform.system().lower()

    if system == 'linux':
        return ['gcc']
        
    return []

@early()
def variants():
    from rez.package_py_utils import expand_requires
    
    # Resolves to platform, arch, and os packages
    requires = ["platform-**", "arch-**", "os-**"]

    requires.append("python-3.11")

    return [expand_requires(*requires)]

def commands():
    appendenv('LD_LIBRARY_PATH', '{root}/lib/')
    appendenv('BOOST_ROOT', '{root}')



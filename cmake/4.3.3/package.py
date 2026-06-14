# -*- coding: utf-8 -*-

name = 'cmake'

version = '4.3.3'

tools = ['cmake', 'cpack', 'ctest']

@early()
def variants():
    from rez.package_py_utils import expand_requires
    
    # Resolves to platform, arch, and os packages
    requires = ["platform-**", "arch-**", "os-**"]

    return [expand_requires(*requires)]

@early()
def private_build_requires():
	import platform
	system = platform.system().lower()

	requires = ['cmake', '!cmake-{}'.format(this.version)]
    
	if system == 'linux':
		requires.append('gcc')
		
	return requires

def commands():
	env.PATH.append("{root}/bin")

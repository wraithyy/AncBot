import py2exe.py2exe_util
from py2exe.py2exe_util import add_resource
import os


def add_resource_patch(name, *arg, **kwarg):
    name_tmp = name + ".tmp"
    os.rename(name, name_tmp)
    add_resource(name_tmp, *arg, **kwarg)
    os.rename(name_tmp, name)


py2exe.py2exe_util.add_resource = add_resource_patch

from distutils.core import setup
import py2exe

from distutils.core import setup
import py2exe

setup(console=["ancbot.py"])

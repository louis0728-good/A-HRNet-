import os
from os.path import join as pjoin
from setuptools import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
import numpy as np

try:
    numpy_include = np.get_include()
except AttributeError:
    numpy_include = np.get_numpy_include()


ext_modules = [
    Extension(
        "cpu_nms",
        ["cpu_nms.pyx"],
        include_dirs = [numpy_include]
    ) # 把隔壁 linux 的抄過來，但只用 cpu 就好
]

setup(
    name='nms_cpu_only',
    ext_modules=ext_modules,
    cmdclass={'build_ext': build_ext},
)
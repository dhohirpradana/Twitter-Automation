from distutils.core import setup

from Cython.Build import cythonize

setup(name='Twitter', ext_modules=cythonize('app.pyx'))

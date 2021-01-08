from setuptools import Extension, setup, find_packages
import os


coast_dir = os.environ['COAST_DIR']
include_flags = f'-I{coast_dir}/include'


pycoast_ext = Extension(
    "pycoast._coast_wrapper",
    sources=['src/coast_wrapper_ext/coast_swig_wrap.cpp'],
    swig_opts=[include_flags],
    library_dirs=[coast_dir + '/lib'],
    libraries=['CorsikaFileIO', 'CorsikaIntern'],
    extra_compile_args=[include_flags],
)


setup(
    name='pycoast',
    version='0.0.1',
    author='Igor Vaiman',
    author_email='gosha.vaiman@gmail.com',
    description='Python interface for COAST tool generated with SWIG',
    package_dir={'pycoast': 'src'},
    packages=['pycoast'],
    ext_modules=[pycoast_ext],
)

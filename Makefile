SWIG_PYFILES = src
SWIG_CPPFILES = src/coast_wrapper_ext

SWIG_INCLUDE = -I${COAST_DIR}/include -Isrc


.PHONY: install clean prepare_swig_dirs

prepare_swig_dirs:
	rm -rf ${SWIG_CPPFILES}
	mkdir ${SWIG_CPPFILES}
	mkdir -p ${SWIG_PYFILES}


install-full: prepare_swig_dirs
	swig -c++ -python -outdir ${SWIG_PYFILES} -o ${SWIG_CPPFILES}/coast_swig_wrap.cpp ${SWIG_INCLUDE} src/coast_swig.i
	python setup.py install


install:
	python setup.py install


DEBUG_OPTS = "-debug-typemap"


debug-swig:
	mkdir -p temp
	swig -c++ -python -outdir temp -o temp/coast_swig_wrap.cpp ${SWIG_INCLUDE} ${DEBUG_OPTS} src/coast_swig.i
	rm -rf temp


clean:
	pip uninstall pycoast -y
	python setup.py clean --all
	rm -rf dist pycoast.egg-info

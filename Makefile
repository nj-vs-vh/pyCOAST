SWIG_PYFILES = "src"
SWIG_CPPFILES = "src/coast_wrapper_ext"


.PHONY: install prepare_swig_dirs

prepare_swig_dirs:
	rm -rf ${SWIG_CPPFILES}
	mkdir ${SWIG_CPPFILES}
	# rm -rf ${SWIG_PYFILES}
	mkdir -p ${SWIG_PYFILES}


install: prepare_swig_dirs
	swig -c++ -python -outdir ${SWIG_PYFILES} -o ${SWIG_CPPFILES}/coast_swig_wrap.cpp -I${COAST_DIR}/include src/coast_swig.i
	python setup.py install

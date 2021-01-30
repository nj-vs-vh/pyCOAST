INCLUDE = -I${COAST_DIR}/include/ -I..
LIBS = -L ${COAST_DIR}/lib/ -lCorsikaFileIO -lCorsikaIntern -L .. -lcorsika2geant

example_build:
	g++ ${INCLUDE} example.cpp ${LIBS} -o example

n_e_mu_build:
	g++ ${INCLUDE} Ne_Nmu_counts.cpp ${LIBS} -o Ne_Nmu_counts

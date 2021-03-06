# `pycoast` — Python wrapper for **CO**rsika data **A**cces**S** **T**ools ([COAST](https://web.ikp.kit.edu/rulrich/coast.html))

Reading CORSIKA runs, showers and particles data from `DATnnnnnn` binary files.

Uses [SWIG](http://www.swig.org/)-generated interface for C++ classes wrapped in custom Python classes for nice idiomatic code.


## Installation

1. Install COAST
   1. [Download](https://web.ikp.kit.edu/rulrich/coast-files/coast-v4r5.tar.gz) and unpack tar archive
  
   2. Create directory for COAST libraries and headers, store its path in `COAST_DIR`, 

   ```bash
   mkdir /my/coast/build
   export COAST_DIR=/my/coast/build
   ```

   3. Run following commands from COAST dir
   ```bash
   ./configure
   make
   make check
   make install
   ```

2. Clone this repository
3. Create Python virtual environment (for example, `python3 -m venv coastenv`)
4. Add following lines with your COAST dir path in virtual environment activation script (e.g. `coastenv/bin/activate`) or in `.bashrc`

```bash
export COAST_DIR=/my/coast/build
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$COAST_DIR/lib
```

5. Run `make install`
6. Run `demo.py` to make sure `pycoast` works

Simple tool to extract particle data from CORSIKA dat files

# Stadalone

`corsika2geant` may be used just to read data and print formatted output to stdout

## build

```bash
make standalone
```

## run

```bash
# print only shower metadata
./corsika2geant_example <file path>
# print every particle params
./corsika2geant_example -v <file path>
```

# Shared library

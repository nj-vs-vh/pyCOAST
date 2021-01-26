Simple program to extract particle data from CORSIKA dat files and print to stdout

## build

```bash
cd corsika2geant
make build
```

## run

```bash
# print only shower metadata
./corsika2geant_example <file path>
# print every particle params
./corsika2geant_example -v <file path>
```

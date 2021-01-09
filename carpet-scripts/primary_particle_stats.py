from pathlib import Path

from pycoast import CorsikaReader

DAT_FILES_DIR = Path('/storage/vol4/ksenia/CORSIKA_LIBRARY/PHOTONS')


thetas = []
phis = []
zfs = []


for dat_file in DAT_FILES_DIR.iterdir():
    if not dat_file.is_file():
        continue

    reader = CorsikaReader(dat_file, verbosity=3)

    for run in reader.runs():
        for shower in run.showers():
            thetas.append(shower.theta)
            phis.append(shower.phi)
            zfs.append(shower.z_first)


print('Z First:\n')
print('\n'.join(str(i) for i in zfs))
print('\n==========================\n\n')
print('Coords:\n')
print('\n'.join(f"{th}, {ph}" for th, ph in zip(thetas, phis)))

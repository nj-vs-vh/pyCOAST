from pathlib import Path
import numpy as np
import termplotlib as tpl

from pycoast import CorsikaReader

DAT_FILES_DIR = Path('./data')


thetas = []
phis = []
zfs = []


for dat_file in DAT_FILES_DIR.iterdir():
    if not dat_file.is_file():
        continue

    reader = CorsikaReader(str(dat_file), verbosity=3)

    for run in reader.runs():
        for shower in run.showers():
            thetas.append(shower.theta)
            phis.append(shower.phi)
            zfs.append(shower.z_first)


print('Z First:\n')
print('\n'.join(str(i) for i in zfs))

counts, bin_edges = np.histogram(zfs)
fig = tpl.figure()
fig.hist(counts, bin_edges, force_ascii=False)
fig.show()

print('\n==========================\n\n')
print('Coords:\n')
print('\n'.join(f"{th}, {ph}" for th, ph in zip(thetas, phis)))

counts, bin_edges = np.histogram(thetas)
fig = tpl.figure()
fig.hist(counts, bin_edges, force_ascii=False)
fig.show()
print(f"thetas between {np.min(thetas)} and {np.max(thetas)}")

counts, bin_edges = np.histogram(phis)
fig = tpl.figure()
fig.hist(counts, bin_edges, force_ascii=False)
fig.show()
print(f"phis between {np.min(phis)} and {np.max(phis)}")

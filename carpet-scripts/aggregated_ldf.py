from pathlib import Path
from tqdm import tqdm
import numpy as np
from math import pi

from matplotlib import pyplot as plt

from pycoast import CorsikaReader

DAT_FILES_DIR = Path('./data')
TEMP_FILES = Path('./temp-data/photons')
TEMP_FILES.mkdir(exist_ok=True)


def temp_filename(data_filename: str, run, shower) -> str:
    return f'{data_filename}_run_{int(run.id)}_shower_{shower.number}_e_p_ldf_hist.dat'


THETA_MAX = 0.35  # ~20 deg
E_PLUS_ID = 2
E_MINUS_ID = 3


bin_count = 60
rad_bin_counts = np.zeros((bin_count,))
rad_bin_counts_squared = np.zeros_like(rad_bin_counts)
rad_bin_edges = np.logspace(0, 3, bin_count + 1)  # m

ring_areas = pi * (np.power(rad_bin_edges[1:], 2) - np.power(rad_bin_edges[:-1], 2))  # m ^ 2


dat_file_paths = [f for f in DAT_FILES_DIR.iterdir() if f.is_file()]
showers_count = 0
SHOWER_META_FNAME = TEMP_FILES / 'meta.dat'

fig, ax = plt.subplots()

for dat_file in tqdm(dat_file_paths):
    reader = CorsikaReader(str(dat_file), verbosity=0)
    for run in reader.runs():
        for shower in run.showers():
            temp_file = temp_filename(dat_file.name, run, shower)
            with open(SHOWER_META_FNAME, 'a') as metadat_file:
                metadat_file.write(f"{temp_file}, {shower.energy}, {shower.theta}, {shower.z_first}\n")

            if shower.theta > THETA_MAX:
                continue
            showers_count += 1

            if (TEMP_FILES / temp_file).exists():
                # reading cached file
                with open(TEMP_FILES / temp_file) as f:
                    f.readline()
                    new_rad_bin_counts = []
                    for line in f:
                        new_rad_bin_counts.append(int(line.split()[2]))
                    new_rad_bin_counts = np.array(new_rad_bin_counts)
            else:
                shower_x = []
                shower_y = []
                for particle in shower.particle_coords():
                    if particle.id == E_PLUS_ID or particle.id == E_MINUS_ID:
                        shower_x.append(particle.x / 100)  # cm -> m
                        shower_y.append(particle.y / 100)  # cm -> m

                particle_radii = np.sqrt(np.power(np.array(shower_x), 2) + np.power(np.array(shower_y), 2))
                new_rad_bin_counts, _ = np.histogram(particle_radii, rad_bin_edges, density=False)
                with open(TEMP_FILES / temp_file, 'w') as f:
                    f.write('rad_min\trad_max\tcount\n')
                    for rad_min, rad_max, count in zip(rad_bin_edges[:-1], rad_bin_edges[1:], new_rad_bin_counts):
                        f.write(f"{rad_min}\t{rad_max}\t{count}\n")

            ax.plot(rad_bin_edges[:-1], new_rad_bin_counts)
            rad_bin_counts += new_rad_bin_counts
            rad_bin_counts_squared += np.power(new_rad_bin_counts, 2)

rad_bin_counts_mean = rad_bin_counts / showers_count

bias_correction = (showers_count / (showers_count-1))
# bias_correction = 1  # for local testing
rad_bin_counts_std = np.sqrt(  # M[x^2] - M[x]^2
    bias_correction * ((rad_bin_counts_squared / showers_count) - np.power(rad_bin_counts_mean, 2))
)

rad_area_densities_mean = rad_bin_counts_mean / ring_areas
rad_area_densities_std = rad_bin_counts_std / ring_areas

rad_bin_centers = 0.5 * (rad_bin_edges[:-1] + rad_bin_edges[1:])

# fig, ax = plt.subplots()
# ax.plot(rad_bin_centers, rad_area_densities_mean, color='red')
# ax.fill_between(
#     rad_bin_centers,
#     rad_area_densities_mean-rad_area_densities_std,
#     rad_area_densities_mean+rad_area_densities_std,
#     alpha=0.3, color='red'
# )
# ax.y_scale('log')
ax.set_yscale('log')
ax.set_xscale('log')
fig.savefig('photon_shower_stacked_e_p_ldf_test.png')

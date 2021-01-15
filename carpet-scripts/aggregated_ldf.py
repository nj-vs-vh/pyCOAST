from pathlib import Path
from tqdm import tqdm
import numpy as np
from math import pi

from matplotlib import pyplot as plt

from pycoast import CorsikaReader

DAT_FILES_DIR = Path('./data')
TEMP_FILES = Path('./temp-data/photons')
TEMP_FILES.mkdir(exist_ok=True)

THETA_MAX = 0.35  # ~20 deg
E_PLUS_ID = 2
E_MINUS_ID = 3


bin_count = 60
radii_bin_counts = np.zeros((bin_count,))
radii_bin_counts_squared = np.zeros_like(radii_bin_counts)
radii_bin_edges = np.logspace(0, 3, bin_count + 1)  # m

ring_areas = pi * (np.power(radii_bin_edges[1:], 2) - np.power(radii_bin_edges[:-1], 2))  # m ^ 2


dat_file_paths = [f for f in DAT_FILES_DIR.iterdir() if f.is_file()]
showers_count = 0

for dat_file in tqdm(dat_file_paths):
    reader = CorsikaReader(str(dat_file), verbosity=0)
    for run in reader.runs():
        for shower in run.showers():
            if shower.theta > THETA_MAX:
                continue
            showers_count += 1
            shower_x = []
            shower_y = []
            for particle in shower.particle_coords():
                if particle.id == E_PLUS_ID or particle.id == E_MINUS_ID:
                    shower_x.append(particle.x / 100)  # cm -> m
                    shower_y.append(particle.y / 100)  # cm -> m

            particle_radii = np.sqrt(np.power(np.array(shower_x), 2) + np.power(np.array(shower_y), 2))
            new_counts, _ = np.histogram(particle_radii, radii_bin_edges, density=False)
            with open(TEMP_FILES / (str(dat_file.name) + '_e_p_ldf_hist.dat'), 'w') as f:
                f.write('rad_min\trad_max\tcount\n')
                for rad_min, rad_max, count in zip(radii_bin_edges[:-1], radii_bin_edges[1:], new_counts):
                    f.write(f"{rad_min}\t{rad_max}\t{count}\n")

            radii_bin_counts += new_counts
            radii_bin_counts_squared += np.power(new_counts, 2)

radii_bin_counts_mean = radii_bin_counts / showers_count

bias_correction = (showers_count / (showers_count-1))
# bias_correction = 1  # for local testing
radii_bin_counts_std = np.sqrt(  # M[x^2] - M[x]^2
    bias_correction * ((radii_bin_counts_squared / showers_count) - np.power(radii_bin_counts_mean, 2))
)

radii_area_densities_mean = radii_bin_counts_mean / ring_areas
radii_area_densities_std = radii_bin_counts_std / ring_areas

radii_bin_centers = 0.5 * (radii_bin_edges[:-1] + radii_bin_edges[1:])

fig, ax = plt.subplots()
ax.plot(radii_bin_centers, radii_area_densities_mean, color='red')
ax.fill_between(
    radii_bin_centers,
    radii_area_densities_mean-radii_area_densities_std,
    radii_area_densities_mean+radii_area_densities_std,
    alpha=0.3, color='red'
)
# ax.y_scale('log')
ax.set_yscale('log')
ax.set_xscale('log')
fig.savefig('photon_shower_stacked_e_p_ldf_test.png')

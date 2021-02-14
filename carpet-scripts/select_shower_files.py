"""Select CORSIKA files based on energy and theta cuts"""

from pathlib import Path
from math import pi
from tqdm import tqdm

from pycoast import CorsikaReader

DAT_FILES_DIR = Path('./data/proton-primary')
total_files = len(list(DAT_FILES_DIR.glob('*')))

FILES_METADATA_FILE = Path('corsika_files_metadata.tsv')
FILE_NAMES_FILE = Path('corsika_files.txt')


E_MIN = 10**5  # GeV
E_MAX = 10**6  # GeV
THETA_MAX = pi * 50 / 180  # 50 deg


with open(FILES_METADATA_FILE, 'w') as meta, open(FILE_NAMES_FILE, 'w') as names:
    meta.write('filename\tID0\tE0\ttheta0\tphi0\n')
    for dat_file in tqdm(DAT_FILES_DIR.iterdir(), total=total_files):
        if not dat_file.is_file():
            continue

        reader = CorsikaReader(str(dat_file), verbosity=0)

        for run in reader.runs():
            for shower in run.showers():
                if shower.energy > E_MIN and shower.energy < E_MAX and shower.theta < THETA_MAX:
                    names.write(f"{dat_file.name}\n")
                    meta.write(
                        f"{dat_file.name}\t{shower.particle_id}\t{shower.energy}\t{shower.theta}\t{shower.phi}\n"
                    )

print('done!')

from pathlib import Path
import matplotlib.pyplot as plt
from tqdm import tqdm

METADATA_FILE = Path('selected_proton_files_metadata.tsv')
DATA_FILES_PATH = Path('data/proton-primary/')

energies = []
file_sizes = []

with open(METADATA_FILE, 'r') as metadata:
    metadata.readline()
    for line in tqdm(metadata):
        line_data = line.split('\t')
        file_name = line_data[0]

        energies.append(float(line_data[2]))
        file_sizes.append((DATA_FILES_PATH / file_name).stat().st_size)


plt.plot(energies, file_sizes, '.')
plt.yscale('log')
plt.ylabel('file size, byte')
plt.xscale('log')
plt.xlabel('energy, GeV')
plt.savefig('energy-vs-file-size-protons.png')

"""Postprocessing for select_shower_files.py: look at selected files, calculate total size, tar if necessary etc"""

from pathlib import Path


FILE_LIST_FILENAME = Path('selected_photon_files.txt')
DATA_DIR = Path('./data/photon-primary')

total_size = 0

with open(FILE_LIST_FILENAME, 'r') as f:
    for line in f:
        current_file = DATA_DIR / line.strip()
        if not current_file.exists():
            raise ValueError(f'Selected file (i.e. listed in {FILE_LIST_FILENAME}) does not seem to exist!')
        stat = current_file.stat()
        total_size += stat.st_size

conv = 1024

print(f"Total size is {total_size / conv**2:.2}M, {total_size / conv**3:.2f}G")

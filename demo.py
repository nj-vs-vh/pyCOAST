from pprint import pprint

import pycoast


DAT_FILE = '/home/njvh/51PH20DAT000000'

reader = pycoast.CorsikaReader(DAT_FILE, verbosity=3)

for run in reader.runs():
    print(run)

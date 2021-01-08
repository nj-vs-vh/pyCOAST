import pycoast


DAT_FILE = '/home/njvh/51PH20DAT000000'

reader = pycoast.CorsikaReader(DAT_FILE, verbosity=3)

for run in reader.runs():
    print(run)
    for shower in run.showers():
        print(shower)
        for i, block in enumerate(shower.subblocks()):
            block.particles()
            if i > 20:
                break

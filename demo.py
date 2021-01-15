import pycoast


DAT_FILE = '/home/njvh/51PH20DAT000000'

reader = pycoast.CorsikaReader(DAT_FILE, verbosity=3)

for run in reader.runs():
    print(run)
    for shower in run.showers():
        print(shower)
        # explicitly reading block-by-block
        for i, block in enumerate(shower.subblocks()):
            for pc in block.particle_coords():
                print(pc)
            if i >= 3:
                break

del reader

reader = pycoast.CorsikaReader(DAT_FILE, verbosity=3)

for run in reader.runs():
    print(run)
    for shower in run.showers():
        print(shower)
        # reading all particle from shower
        for i, pc in enumerate(shower.particle_coords()):
            print(i, "\t", pc)
            if i >= 20:
                break

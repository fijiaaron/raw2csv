import numpy
import rawpy
import PIL

from os import path
import sys

# get input filename
if len(sys.argv) != 2:
    print("usage: raw2csv filename.dng")
    sys.exit(1)

dngfile = sys.argv[1]

if not path.exists(dngfile):
    print("DNG file does not exist:", dngfile)
    sys.exit(1)

# set output filename
file, ext = path.splitext(dngfile)
csvfile = file + ".csv"
print("writing csvfile: " + csvfile)

# convert file
raw = rawpy.imread(dngfile)
rawdata = raw.raw_image
numpy.savetxt(csvfile, rawdata, delimiter=",")
raw.close()

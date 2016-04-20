import numpy as np
import sys
import os

from cook4ml import Cook
from cook4ml.storage.hdf5 import HDF5
from cook4ml.data.image import ImagePatch


if __name__ == "__main__":
    if len(sys.argv) < 8:
        print 'generate_im2im.py <patch_size> <num_channels> <stride>' \
            '<batch_size> <db_filename> <x_directory> <y_directory>'
        sys.exit(2)

    shape = (int(sys.argv[1]), int(sys.argv[1]), int(sys.argv[2]))
    stride = int(sys.argv[3])
    batch_size = int(sys.argv[4])
    db_filename = os.path.join(os.getcwd(), sys.argv[5])
    x_directory = os.path.join(os.getcwd(), sys.argv[6])
    y_directory = os.path.join(os.getcwd(), sys.argv[7])

    cook = Cook(HDF5(db_filename))
    cook.add(ImagePatch('x', shape, stride, x_directory))
    cook.add(ImagePatch('y', shape, stride, y_directory))
    cook.prepare(batch_size=batch_size)

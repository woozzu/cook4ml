import numpy as np
import h5py

from cook4ml.storage import BaseStorage


class HDF5(BaseStorage):

    def __init__(self, filename):
        super(HDF5, self).__init__()
        self.filename = filename

    def open_(self):
        self.file = h5py.File(self.filename, 'w')

    def close(self):
        self.file.close()

    def _alloc_field(self, name, shape):
        return self.file.create_dataset(name, tuple([0]) + tuple(shape), maxshape=tuple([None]) + tuple(shape))

    def _push_back(self, field, cursor, data):
        new_cursor = cursor + data.shape[0]
        field.resize(new_cursor, 0)
        field[cursor:new_cursor, ...] = data

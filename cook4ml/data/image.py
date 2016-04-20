import os
import numpy as np
import skimage.io

from cook4ml.data import BaseData
from cook4ml.utils.image_utils import slice_patch


class ImagePatch(BaseData):

    def __init__(self, name, shape, stride, img_dir):
        if shape[0] != shape[1]:
            raise ValueError('ImagePatch supports only square shape.')
        super(ImagePatch, self).__init__(name, shape)
        self.stride = stride
        self.img_dir = img_dir

    def prepare(self, batch_callback, batch_size=1000000):
        self.__batch_callback = batch_callback
        filenames = os.listdir(self.img_dir)
        for filename in filenames:
            path = os.path.join(self.img_dir, filename)
            if os.path.isdir(path):
                continue
            img = skimage.io.imread(path)
            if img.shape == (2,):
                img = img[0]
            img = img.astype('float')
            slice_patch(img, self.shape[0], self.stride,
                        self.__callback, batch_size)

    def __callback(self, data):
        self.__batch_callback(self.name, data)

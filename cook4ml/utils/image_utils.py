import numpy as np


def slice_patch(img, patch_size, stride, batch_callback, batch_size=128):
    if len(img.shape) < 3:
        n_channel = 1
    else:
        n_channel = img.shape[2]
    data = np.zeros(tuple([batch_size]) + (patch_size, patch_size, int(n_channel)))
    offset = 0
    for i in xrange(0, img.shape[0], stride):
        if i + patch_size >= img.shape[0]:
            continue

        for j in xrange(0, img.shape[1], stride):
            if j + patch_size >= img.shape[1]:
                continue

            data[offset, ...] = img[i:i + patch_size, j:j + patch_size, :]
            offset = offset + 1

            if offset == batch_size:
                batch_callback(data)
                offset = 0

    if offset > 0:
        batch_callback(data[0:offset, ...])


def merge_patch():
    pass

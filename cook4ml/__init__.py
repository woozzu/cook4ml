import numpy as np


class Cook(object):

    def __init__(self, storage):
        self.storage = storage
        self.storage.__enter__()
        self.data = []

    def add(self, data):
        self.data.append(data)
        self.storage.add(data.name, data.shape)

    def prepare(self, batch_size=1000000, batch_shuffle=True, seed=None):
        self.__batch_shuffle = batch_shuffle
        if self.__batch_shuffle:
            np.random.seed(seed)
            self.r_state = list(np.random.get_state())
        
        for d in self.data:
            if self.__batch_shuffle:
                self.r_state[2] = 0
                np.random.set_state(self.r_state)
            d.prepare(self.__save_batch, batch_size)

        self.storage.__exit__()

    def __save_batch(self, name, batch):
        if self.__batch_shuffle:
            perm = np.random.permutation(batch.shape[0])
            batch = batch[perm, ...]
        self.storage.push_back(name, batch)

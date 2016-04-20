import numpy as np


class BaseStorage(object):

    def __init__(self):
        self.__field = {}
        self.__cursor = {}

    def __enter__(self):
        self.open_()

    def __exit__(self):
        self.close()

    def open_(self):
        pass

    def close(self):
        pass

    def add(self, name, shape):
        self.__field[name] = self._alloc_field(name, shape)
        self.__cursor[name] = 0

    def _alloc_field(self, name, shape):
        raise NotImplementedError()

    def push_back(self, name, data):
        self._push_back(self.__field[name], self.__cursor[name], data)
        self.__cursor[name] = self.__cursor[name] + data.shape[0]

    def _push_back(self, field, cursor, data):
        raise NotImplementedError()


class Memory(BaseStorage):

    def __init__(self):
        super(Memory, self).__init__()

    def _alloc_field(self, name, shape):
        pass

    def _push_back(self, field, data):
        pass

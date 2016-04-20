

class BaseData(object):

    def __init__(self, name, shape):
        self.name = name
        self.shape = shape

    def prepare(self, batch_callback, batch_size=1000000):
        raise NotImplementedError()

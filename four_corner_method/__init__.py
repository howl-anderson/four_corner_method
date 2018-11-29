import pickle

import pkg_resources


class FourCornerMethod(object):
    def __init__(self):
        data_file = pkg_resources.resource_filename(__name__, "data/data.pkl")

        with open(data_file, 'rb') as fd:
            self.data = pickle.load(fd)

    def query(self, input_char, default=None):
        return self.data.get(input_char, default)


if __name__ == "__main__":
    fcm = FourCornerMethod()
    result = fcm.query('名')

    print(result)

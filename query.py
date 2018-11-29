import pickle
import sys


def query(input_char):
    with open('four_corner_method/data/data.pkl', 'rb') as fd:
        data = pickle.load(fd)

    return data.get(input_char)


if __name__ == "__main__":
    input_char = sys.argv[1]

    result = query(input_char)

    print(result)

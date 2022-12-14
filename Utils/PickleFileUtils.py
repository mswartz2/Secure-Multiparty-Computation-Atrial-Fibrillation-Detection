import pickle
import os


def write_to_pickle_file(data, filename):
    # make directory two levels higher
    if not os.path.exists(os.path.dirname(os.path.dirname(filename))):
        os.makedirs(os.path.dirname(os.path.dirname(filename)))

    # make directory one level higher
    if not os.path.exists(os.path.dirname(filename)):
        os.makedirs(os.path.dirname(filename))

    pickle_file = open(filename, "wb")
    pickle.dump(data, pickle_file)
    pickle_file.close()


def read_in_pickle_file(filename):
    with open(filename, "rb") as myfile:
        data = pickle.load(myfile)

    return data

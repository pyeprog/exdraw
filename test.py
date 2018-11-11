import _pickle as pkl
from uuid import uuid4


def save_mock_pickle_file():
    example_str = "This is an example"
    name = uuid4()
    with open("./watching/{}".format(name), "wb") as fp:
        pkl.dump(example_str, fp)


if __name__ == '__main__':
    save_mock_pickle_file()

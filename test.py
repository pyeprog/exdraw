import sys
import _pickle as pkl
from uuid import uuid4
from random import randint
from shapely.geometry import Polygon
from shapely.affinity import translate

from config import info_dict


def save_mock_pickle_file():
    example_str = "This is an example"
    name = uuid4()
    with open("./watching/{}".format(name), "wb") as fp:
        pkl.dump(example_str, fp)

def get_random_polygon(unit_size:int=10):
    return Polygon([(-randint(1, unit_size), randint(1, unit_size)),
                    (-randint(1, unit_size), -randint(1, unit_size)),
                    (randint(1, unit_size), -randint(1, unit_size)),
                    (randint(1, unit_size), randint(1, unit_size))])

def get_random_separated_polygon(unit_size:int=10, separate_length:int=10):
    random_polygon = get_random_polygon(unit_size)
    x_offset = randint(-separate_length, separate_length)
    y_offset = randint(-separate_length, separate_length)
    return translate(random_polygon, x_offset, y_offset)

def draw_single_shapely():
    example_geom = get_random_polygon()
    name = uuid4()
    with open("./watching/{}".format(name), "wb") as fp:
        pkl.dump((info_dict["func_type"].draw_single_shapely, example_geom), fp)

def draw_shapely_one_by_one():
    example_geoms = [get_random_polygon() for _ in range(10)]
    name = uuid4()
    with open("./watching/{}".format(name), "wb") as fp:
        pkl.dump((info_dict["func_type"].draw_shapely_one_by_one, example_geoms), fp)

def draw_all_shapely():
    example_geoms = [get_random_separated_polygon(10, 50) for _ in range(10)]
    name = uuid4()
    with open("./watching/{}".format(name), "wb") as fp:
        pkl.dump((info_dict["func_type"].draw_all_shapely, example_geoms), fp)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        if sys.argv[1] == "0":
            draw_single_shapely()
        elif sys.argv[1] == "1":
            draw_shapely_one_by_one()
        else:
            draw_all_shapely()

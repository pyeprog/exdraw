import _pickle as pkl
import os
from random import randint
from uuid import uuid4

from shapely.geometry import Polygon
from shapely.wkt import dump

from config.local import LocalConfig

__all__ = ["mock_local_save_polygon"]


def _get_file_path():
    filename = str(uuid4())
    file_path = os.path.join(LocalConfig.WATCH_PATH, filename)
    return file_path


def _dump(obj):
    with open(_get_file_path(), "w") as fp:
        pkl.dump(obj, fp)


def _shapely_dump(obj):
    with open(_get_file_path(), "w") as fp:
        dump(obj, fp)


def mock_local_save_polygon():
    start_p = (0, 0)
    first_p = (randint(0, 3), randint(0, 5))
    second_p = (randint(4, 7), randint(3, 6))
    end_p = (10, 0)
    p_list = [start_p, first_p, second_p, end_p]
    eg_polygon = Polygon(p_list)
    _shapely_dump(eg_polygon)

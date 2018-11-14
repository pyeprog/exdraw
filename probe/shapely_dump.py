import os
import _pickle as pkl
from uuid import uuid4


# load watching path
config_file_path = os.path.join(os.path.dirname(__file__), "config")
with open(config_file_path, "rb") as fp:
    info_dict = pkl.load(fp)

watching_path = info_dict.get("watching_path", "")
FuncType = info_dict.get("func_type")


def _dump_obj(func_type, obj):
    name = str(uuid())
    with open(os.path.join(watching_path, name), "wb") as fp:
        pkl.dump((func_type, obj), fp)

def draw_single_shapely(geom):
    _dump_obj(FuncType.draw_single_shapely, geom)

def draw_shapely_one_by_one(geoms):
    _dump_obj(FuncType.draw_shapely_one_by_one, geoms)

def draw_all_shapely(geoms):
    _dump_obj(FuncType.draw_all_shapely, geoms)

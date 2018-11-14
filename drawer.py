import math
import numpy as np
import matplotlib.pyplot as plt
from config import FuncType
from geopandas import GeoSeries

color_map = ["tab10", "tab20", "Accent", "Dark2", "Paired", "Pastel1", "Set1", "Set2"]

class Drawer(object):
    @staticmethod
    def draw_single_shapely(geom):
        if isinstance(geom, (list, tuple)):
            print("\tDraw_single_shapely could only handle single geometry")
            return
        GeoSeries([geom]).plot(ax=plt.gca())
        plt.show()

    @staticmethod
    def draw_shapely_one_by_one(geoms):
        if len(geoms) == 0:
            print("\tNo geometry provided")
        n_rows = math.ceil(len(geoms) / 4)
        n_cols = 4 if n_rows > 1 else len(geoms)
        plt.figure()
        fig, axs = plt.subplots(figsize=[n_cols*3.2, n_rows*2.4], ncols=n_cols, nrows=n_rows, sharex=True, sharey=True)
        if isinstance(axs, np.ndarray):
            axs = axs.flatten()
        print("\tTotal {} geoms drawn".format(len(geoms)))
        for geom, cur_ax in zip(geoms, axs):
            GeoSeries([geom]).plot(ax=cur_ax)
        plt.show()

    @staticmethod
    def draw_all_shapely(geoms):
        print("\tTotal {} geoms drawn".format(len(geoms)))
        GeoSeries(geoms).plot(ax=plt.gca(), cmap=color_map[0])
        plt.show()

func_type_to_func = {FuncType["draw_single_shapely"]: Drawer.draw_single_shapely,
                     FuncType["draw_shapely_one_by_one"]: Drawer.draw_shapely_one_by_one,
                     FuncType["draw_all_shapely"]: Drawer.draw_all_shapely}

def get_drawer(func_type: FuncType):
    return func_type_to_func[func_type]

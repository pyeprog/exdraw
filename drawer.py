import math
from random import choice, randint
import numpy as np
import matplotlib.pyplot as plt
from config import FuncType
from geopandas import GeoSeries, GeoDataFrame

color_map_name = ["tab10", "tab20", "Accent", "Dark2", "Paired", "Pastel1", "Set1", "Set2"]
tab10_color = ["tab:blue", "tab:orange", "tab:green", "tab:red", "tab:purple", "tab:brown", "tab:pink",
               "tab:gray", "tab:olive", "tab:cyan"]

class Drawer(object):
    @staticmethod
    def draw_single_shapely(geom):
        if isinstance(geom, (list, tuple)):
            print("\tDraw_single_shapely could only handle single geometry")
            return
        GeoSeries([geom]).plot(ax=plt.gca(), cmap=color_map_name[0])
        plt.show()

    @staticmethod
    def draw_shapely_one_by_one(geoms):
        if len(geoms) == 0:
            print("\tNo geometry provided")
            return
        if len(geoms) <= 16:
            n_rows = math.ceil(len(geoms) / 4)
            n_cols = 4 if n_rows > 1 else len(geoms)
        else:
            n_rows = math.ceil(len(geoms) / 6)
            n_cols = 6 if n_rows > 1 else len(geoms)

        fig, ax_array = plt.subplots(nrows=n_rows, ncols=n_cols)
        fig.set_size_inches(16, 10)
        if isinstance(ax_array, np.ndarray):
            ax_array = np.array(ax_array)

        for i, (geom, ax) in enumerate(zip(geoms, ax_array.flatten())):
            ax.set_aspect("equal")
            if not "Multi" in geom.type:
                seperated_geoms = [geom]
            else:
                seperated_geoms = list(geom)
            for seperate_geom in seperated_geoms:
                if seperate_geom.type == "Polygon":
                    xs, ys = seperate_geom.exterior.xy
                    ax.fill(xs, ys, facecolor=tab10_color[i % len(tab10_color)])
                elif seperate_geom.type == "LineString":
                    xs = [coord[0] for coord in seperate_geom.coords]
                    ys = [coord[1] for coord in seperate_geom.coords]
                    ax.plot(xs, ys)


        plt.show()

    @staticmethod
    def draw_all_shapely(geoms):
        print("\tTotal {} geoms drawn".format(len(geoms)))
        geoms.sort(key=lambda geom: geom.area, reverse=True)
        GeoSeries(geoms).plot(ax=plt.gca(), cmap=color_map_name[0])
        plt.show()

    @staticmethod
    def compare_two_shapely(two_geoms_tuple):
        geoms1, geoms2 = two_geoms_tuple
        geoms1.sort(key=lambda geom: geom.area, reverse=True)
        geoms2.sort(key=lambda geom: geom.area, reverse=True)
        print("Geometry group1: {}\n Geometry group2: {}".format(len(geoms1), len(geoms2)))
        fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, sharex=True, sharey=True, squeeze=True)
        fig.set_size_inches(16, 10)
        GeoSeries(geoms1).plot(ax=ax1, cmap=color_map_name[0])
        GeoSeries(geoms2).plot(ax=ax2, cmap=color_map_name[0])
        plt.show()

func_type_to_func = {FuncType["draw_single_shapely"]: Drawer.draw_single_shapely,
                     FuncType["draw_shapely_one_by_one"]: Drawer.draw_shapely_one_by_one,
                     FuncType["draw_all_shapely"]: Drawer.draw_all_shapely,
                     FuncType["compare_two_shapely"]: Drawer.compare_two_shapely}

def get_drawer(func_type: FuncType):
    return func_type_to_func[func_type]

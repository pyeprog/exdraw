from config import FuncType
import matplotlib.pyplot as plt
from geopandas import GeoSeries


class Drawer(object):
    @staticmethod
    def draw_single_shapely(geom):
        GeoSeries([geom]).plot(ax=plt.gca())
        plt.show()

    @staticmethod
    def draw_shapely_one_by_one(geoms):
        for geom in geoms:
            GeoSeries([geom]).plot(ax=plt.gca())
            plt.show()

    @staticmethod
    def draw_all_shapely(geoms):
        GeoSeries(geoms).plot(ax=plt.gca())
        plt.show()

    @staticmethod
    def mock_draw(dummy):
        print("We draw something")

func_type_to_func = {FuncType.draw_single_shapely: Drawer.draw_single_shapely,
                     FuncType.draw_shapely_one_by_one: Drawer.draw_shapely_one_by_one,
                     FuncType.draw_all_shapely: Drawer.draw_all_shapely}

def get_drawer(func_type: FuncType):
    return func_type_to_func[func_type]

# import matplotlib.pyplot as plt
# from geopandas import GeoSeries


class Drawer(object):
    @staticmethod
    def draw_single_shapely(geom):
        GeoSeries([geom]).plot(ax=plt.gca())
        plt.show()

    @staticmethod
    def mock_draw(dummy):
        print("We draw something")

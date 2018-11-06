import matplotlib.pyplot as plt
# from descartes import PolygonPatch
# from shapely.geometry import LineString, Polygon
from geopandas import GeoSeries


class ShapelyDrawer(object):
    # @classmethod
    # def _draw_line(cls, ax, line: LineString):
    #     x, y = line.xy
    #     ax.plot(x, y, color=DrawColor.GRAY, solid_capstyle='round', zorder=1)


    # @classmethod
    # def _draw_polygon(cls, ax, poly: Polygon):
    #     poly_patch = PolygonPatch(poly, fc=DrawColor.BLUE, ec=DrawColor.BLUE, alpha=0.5, zorder=2)
    #     ax.add_patch(poly_patch)


    @staticmethod
    def draw_geom(geom):
        # todo(pye): Test the draw_geom and make it work
        # print("In draw_geom", geom)
        GeoSeries([geom]).plot(ax=plt.gca())
        ax = plt.gca()
        # ShapelyDrawer._draw_polygon(ax, geom)
        plt.show()


    @staticmethod
    def draw_geoms(geom_list):
        pass

    @staticmethod
    def draw_geoms_one_by_one(geom_list):
        pass

    @staticmethod
    def draw_geoms_in_lattice(geom_list):
        pass

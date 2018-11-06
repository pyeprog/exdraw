import _pickle as pkl
from os.path import isfile
from time import sleep

from watchgod import watch, Change

from config.local import LocalConfig
from draw.draw_shapely import ShapelyDrawer
from process.local_process import LocalProcess


class LocalApp(object):
    def __init__(self, watch_path=None):
        self.watch_path = LocalConfig.WATCH_PATH if watch_path is None else watch_path
        self.register = set()

    def run(self):
        self.start()
        try:
            self.watch(self.main_handler, 1)
        except KeyboardInterrupt:
            self.end()

    def start(self):
        print("DO some preparation")

    def end(self):
        print("DO some cleaning")

    def watch(self, handler, t_interval):
        while True:
            sleep(t_interval)
            handler()

    def main_handler(self):
        print('watching {}'.format(self.watch_path))
        for changes in watch(self.watch_path):
            for op_type, file_path in changes:
                print(op_type, file_path)
                if file_path not in self.register and op_type in {Change.modified, Change.added}:
                    self.register.add(file_path)
                    LocalProcess.do(ShapelyDrawer.draw_geom, self._readfile(file_path))

    @staticmethod
    def _readfile(path):
        assert isfile(path), "Invalid file path"
        with open(path, "rb") as fp:
            content = pkl.load(fp)
        return content

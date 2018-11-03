import _pickle as pkl
from os.path import isfile
from time import sleep, time
from watchgod import watch, Change

from config.local import LocalConfig


class LocalApp(object):
    def __init__(self, watch_path=None):
        self.watch_path = LocalConfig.WATCH_PATH if watch_path is None else watch_path
        self.register = set()
 
    def run(self):
        self.start()
        try:
            self.watch(self.handler, 1)
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

    def handler(self):
        for changes in watch(self.watch_path):
            for op_type, filepath in changes:
                print(op_type, filepath)
                if filepath not in self.register and op_type in {Change.modified, Change.added}:
                    self.register.add(filepath)
                    content = self._readfile(filepath)
                    print(content)

    @staticmethod
    def _readfile(path):
        assert isfile(path), "Invalid file path"
        with open(path, "rb") as fp:
            content = pkl.load(fp)
        return content



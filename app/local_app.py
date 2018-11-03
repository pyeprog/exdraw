import _pickle as pkl
from os.path import isfile
from time import sleep
from watchgod import watch, Change
from multiprocessing import Process

from config.local import LocalConfig


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
        for changes in watch(self.watch_path):
            for op_type, filepath in changes:
                if filepath not in self.register and op_type in {Change.modified, Change.added}:
                    self.register.add(filepath)
                    self.spawn_process(self._readfile(filepath))


    @staticmethod
    def _readfile(path):
        assert isfile(path), "Invalid file path"
        with open(path, "rb") as fp:
            content = pkl.load(fp)
        return content

    @staticmethod
    def spawn_process(content):
        print(content)
        cur_process = Process(target=test_func, args=(content,))
        cur_process.start()
        cur_process.join()

def test_func(*args):
    print(args)

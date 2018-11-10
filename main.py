import os
import _pickle as pkl
from time import sleep
from shutil import copytree, rmtree
from watchgod import Change, watch
from multiprocessing import Process

from drawer import Drawer


class LocalApp(object):
    def __init__(self):
        self.cwd = os.path.dirname(__file__)
        self.inject_path = os.getcwd()
        self.cwd = "./" if len(self.cwd) == 0 else self.cwd
        self.inject_path = "./" if len(self.inject_path) == 0 else self.inject_path
        self.inject_module_path = os.path.join(self.inject_path, "probe")
        self.module_src_path = os.path.join(self.cwd, "_probe")
        self.watching_path = os.path.join(self.cwd, "watching")
        self.probe_config_path = os.path.join(self.module_src_path, "config")
        self.info_dict = {"watching_path": self.watching_path}

    def run(self):
        self._inject_config_to_probe()
        self._setUp()
        while True:
            try:
                self._work()
                sleep(0.5)
            except KeyboardInterrupt:
                break
        self._tearDown()
        self._tear_config_in_probe()
        
    def _setUp(self):
        self._tearDown()
        copytree(self.module_src_path, self.inject_module_path)
        print("Injection done")

    def _inject_config_to_probe(self):
        with open(self.probe_config_path, "wb") as fp:
            pkl.dump(self.info_dict, fp)

    def _tearDown(self):
        if os.path.isdir(self.inject_module_path):
            rmtree(self.inject_module_path)
        print("Cleaning done")

    def _tear_config_in_probe(self):
        if os.path.isfile(self.probe_config_path):
            os.remove(self.probe_config_path)

    def _work(self):
        for changes in watch(self.watching_path):
            for op_type, changed_file_path in changes:
                if op_type == Change.added:
                    self._handler(changed_file_path)

    @staticmethod
    def _handler(file_path):
        try:
            with open(file_path, "rb") as fp:
                content = pkl.load(fp)
            wp = Process(target=Drawer.mock_draw, args=(content,))
            wp.start()
        except:
            return
        

if __name__ == '__main__':
    app = LocalApp()
    app.run()

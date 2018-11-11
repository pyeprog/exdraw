import os
import _pickle as pkl
from time import sleep
from shutil import copytree, rmtree
from watchgod import Change, watch
from multiprocessing import Process

from drawer import Drawer
from config import FuncType, info_dict


class LocalApp(object):
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
        copytree(info_dict["module_src_path"], info_dict["inject_module_path"])
        print("Injection done")

    def _inject_config_to_probe(self):
        with open(info_dict["probe_config_path"], "wb") as fp:
            pkl.dump(info_dict, fp)

    def _tearDown(self):
        if os.path.isdir(info_dict["inject_module_path"]):
            rmtree(info_dict["inject_module_path"])
        print("Cleaning done")

    def _tear_config_in_probe(self):
        if os.path.isfile(info_dict["probe_config_path"]):
            os.remove(info_dict["probe_config_path"])

    def _work(self):
        for changes in watch(info_dict["watching_path"]):
            for op_type, changed_file_path in changes:
                if op_type == Change.added:
                    self._handler(changed_file_path)

    @staticmethod
    def _handler(file_path):
        try:
            with open(file_path, "rb") as fp:
                content = pkl.load(fp)
            func_type, arguments = content
            wp = Process(target=Drawer.get_drawer(func_type), args=(arguments,))
            wp.start()
        except:
            print("The file cannot be read properly")
        

if __name__ == '__main__':
    app = LocalApp()
    app.run()

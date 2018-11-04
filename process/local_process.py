from process.base_process import BaseProcess
from multiprocessing import Process


class LocalProcess(BaseProcess):
    @classmethod
    def do(cls, method, content):
        method(content)


class LocalMultiProcess(BaseProcess):
    @classmethod
    def do(cls, method, content):
        cur_process = Process(target=method, args=(content,))
        cur_process.start()

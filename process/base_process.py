from abc import ABC, abstractmethod


class BaseProcess(ABC):
    @classmethod
    @abstractmethod
    def do(cls):
        raise NotImplementedError("Method do is not implemented")

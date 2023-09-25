from abc import ABC, abstractmethod
import pathlib

WF_DIR = ""
RF_DIR = ""

class Template(ABC):

    @abstractmethod
    def build(self):
        pass

    @abstractmethod
    def modify(self, xml):
        pass
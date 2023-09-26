from abc import ABC, abstractmethod
from rescon import BASE_DIR

TEX_DIR = BASE_DIR + "/templates/tex"

class Template(ABC):

    @abstractmethod
    def build(self):
        pass

    @abstractmethod
    def modify(self, xml):
        pass
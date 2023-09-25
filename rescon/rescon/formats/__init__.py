from abc import ABC, abstractmethod
from rescon import BASE_DIR

OUT_DIR = BASE_DIR + "/templates/tex/out"
IN_DIR = BASE_DIR + "/templates/tex/in"

class Template(ABC):

    @abstractmethod
    def build(self):
        pass

    @abstractmethod
    def modify(self, xml):
        pass
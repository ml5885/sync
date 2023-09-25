from abc import ABC, abstractmethod

class Template(ABC):

    @abstractmethod
    def build(self):
        pass

    @abstractmethod
    def modify(self, xml):
        pass
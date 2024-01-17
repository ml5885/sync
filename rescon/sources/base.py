import requests
from abc import ABC, abstractmethod

class InvalidURLException(Exception):
    pass

class Source(ABC):

    def __init__(self, url, _base=""):
        if not self._valid_url(url, _base):
            raise InvalidURLException("Invalid URL")
        self.url = url

    def _valid_url(self, url, _base):
        if _base not in url: return False
        return requests.get(url).ok

    @abstractmethod
    def get_questions(self, _parser="html.parser"):
        pass
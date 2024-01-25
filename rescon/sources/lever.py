from .base import Source
from bs4 import BeautifulSoup
import requests

class Lever(Source):

    def __init__(self, url, _base="jobs.lever.co"):
        super().__init__(url, _base)
    
    def get_questions(self, _parser="html.parser"):
        lever_html = requests.get(f"{self.url}/apply").content
        bs = BeautifulSoup(lever_html, _parser)
        qs = bs.find_all("li", {"class": "custom-question"})
        pqs = []
        for q in qs:
            textqs = q.find("div", {"class": "application-label"}).find("div", {"class": "text"}).text.strip()
            pqs.append(textqs)
        return textqs
    
    def get_description(self, _parser="html.parser"):
        lever_html = requests.get(self.url).content
        bs = BeautifulSoup(lever_html, _parser)
        content = bs.find("div", {"class": "content"}).get_text()
        return content
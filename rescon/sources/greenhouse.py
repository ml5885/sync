from rescon.sources.base import Source
from bs4 import BeautifulSoup
import requests

class Greenhouse(Source):

    def __init__(self, url, _base="boards.greenhouse.io"):
        super().__init__(url, _base)
    
    def get_questions(self, _parser="html.parser"):
        gh_html = requests.get(self.url).content
        bs = BeautifulSoup(gh_html, _parser)
        qs = bs.find("div", {"id": "custom_fields"}).find_all("div", {"class": "field"})
        textqs = []
        for q in qs:
            hq = q.find("label")
            if hq.find("textarea"): textqs.append(hq.text)
        return textqs
    
    def get_description(self, _parser="html.parser"):
        gh_html = requests.get(self.url).content
        bs = BeautifulSoup(gh_html, _parser)
        content = bs.find("div", {"id": "content"}).get_text()
        return content

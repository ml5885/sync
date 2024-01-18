from .greenhouse import Greenhouse
from .lever import Lever

def switch_scrape(link):
    if "lever" in link: return Lever
    if "greenhouse" in link: return Greenhouse
    return None
import re

class TexTemplate:
    
    def __init__(self, filepath) -> None:
        self.file = open(filepath, "r")
    
    def _convert_to_xml(self, lines):
        XML = {}
        q = []
        for line in lines:
            line = line.strip()
            if not re.match("^{%.*%}$", line):
                continue
            cc = line[2:-2].strip()
            


    def build(self):
        lines = self.file.readlines()
        xml = self._convert_to_xml(lines)

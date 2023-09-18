import re
from collections import defaultdict
import xml.etree.ElementTree as ET

class TexTemplate:
    
    def __init__(self, filepath) -> None:
        self.file = open(filepath, "r")

    def _convert_to_xml(self, lines):
        
        xml = ET.Element("resume")
        curr = xml
        q = []
        i = 0
        data = []

        def handle_tag(tag_line):
            if "begin" in tag_line:
                q.append(tag_line.split()[-1])
                curr = ET.SubElement(curr, q[-1])
            elif "end" in tag_line:
                _ = q.pop()
                curr = curr.getparents()

        while i < len(lines):
            line = lines[i].strip()
            if not re.match("^{%.*%}$", line): continue
            line = line[2:-2].strip()
            if "tag" in line:


            i += 1
        for i, line in lines:
            line = line.strip()



    def build(self):
        lines = self.file.readlines()
        xml = self._convert_to_xml(lines)

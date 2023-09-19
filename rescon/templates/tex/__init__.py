import re
from collections import defaultdict
import xml.etree.ElementTree as ET
import xml.dom.minidom as MD

def find_parent(root, child):
    for parent in root.iter():
        for cn in parent:
            if child != cn:
                continue
            return parent
    return None

def handle_tag(tag_line, curr, q, data, root):
    if "begin" in tag_line:
        q.append(tag_line.split()[-1])
        curr = ET.SubElement(curr, q[-1])
        return curr, q, data, root
    elif "end" in tag_line:
        _ = q.pop()
        if data:
            curr.text = "\n".join(data["stored"])
            data["stored"] = []
        curr = find_parent(root, curr)
        return curr, q, data, root
    raise InvalidTagError()

class InvalidTagError(Exception):
    pass

class TexTemplate:
    
    def __init__(self, filepath) -> None:
        self.file = open(filepath, "r")

    def _convert_to_xml(self, lines):
        
        root = ET.Element("resume")
        curr = root
        q = []
        i = 0
        data = {"en": False, "stored": []}

        while i < len(lines):
            line = lines[i].strip()
            if re.match("^{%.*%}$", line):
                line = line[2:-2].strip()
                if "tag" in line:
                    try:
                        curr, q, data, root = handle_tag(line, curr, q, data, root)
                    except InvalidTagError as e:
                        print(ET.tostring(root))
                elif "DATA" in line:
                    data["en"] = not data["en"]
                i += 1
                continue
            if data["en"]: data["stored"].append(line)
            i += 1
        
        return root

    def _update_tex_with_xml(self, lines):
        
        root = ET.Element("resume")
        curr = root
        q = []
        i = 0
        data = {"en": False, "stored": []}

        while i < len(lines):
            line = lines[i].strip()
            if re.match("^{%.*%}$", line):
                line = line[2:-2].strip()
                if "tag" in line:
                    try:
                        curr, q, data, root = handle_tag(line, curr, q, data, root)
                    except InvalidTagError as e:
                        print(ET.tostring(root))
                elif "DATA" in line:
                    data["en"] = not data["en"]
                i += 1
                continue
            if data["en"]: data["stored"].append(line)
            i += 1
        
        return True

    def build(self):
        lines = self.file.readlines()
        return self._convert_to_xml(lines)

    def modify(self, xml):
        lines = self.file.readlines()
        return self._update_tex_with_xml(lines)
        
        


def main():
    ttm = TexTemplate("/home/tanush/Programming/Projects/rescon/rescon/templates/tex/func.ttx")
    root = ttm.build()
    print(MD.parseString(ET.tostring(root).decode()).toprettyxml())

if __name__ == "__main__":
    main()
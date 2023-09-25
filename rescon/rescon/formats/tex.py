import re
from collections import defaultdict
import xml.etree.ElementTree as ET
import xml.dom.minidom as MD
from datetime import datetime
from ..formats import Template, IN_DIR, OUT_DIR


def find_parent(root, child):
    for parent in root.iter():
        for cn in parent:
            if child != cn:
                continue
            return parent
    return None

def handle_tag_convert(tag_line, curr, q, data, root):
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

def remove_tags(ttx):
    return re.sub("{%.*%}", "", ttx)

class InvalidTagError(Exception):
    pass

class TEXTemplate(Template):
    
    def __init__(self, rf, wf) -> None:
        self.filepath = [rf, wf]

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
                        curr, q, data, root = handle_tag_convert(line, curr, q, data, root)
                    except InvalidTagError as e:
                        print(ET.tostring(root))
                elif "DATA" in line:
                    data["en"] = not data["en"]
                i += 1
                continue
            if data["en"]: data["stored"].append(line)
            i += 1
        
        return root

    def _update_tex_with_xml(self, lines, root):
        ttx = []
        i = j = 0
        for n in root.iter():
            if n.text.isspace(): continue
            while i < len(lines):
                line = lines[i].strip()
                if line == "{% DATA %}":
                    k = i + 1
                    while lines[k].strip() != "{% DATA %}": k += 1
                    ttx.extend(lines[j:i])
                    ttx.append(n.text)
                    j = k + 1
                    i = k + 1
                    break
                i += 1
        ttx.extend(lines[i:])
        return remove_tags("".join(ttx))

    def build(self):
        rf = open(f"{IN_DIR}/{self.filepath[0]}", "r")
        lines = rf.readlines()
        rf.close()
        return self._convert_to_xml(lines)

    def modify(self, xml):
        rf = open(f"{IN_DIR}/{self.filepath[0]}", "r")
        wf = open(f"{OUT_DIR}/{self.filepath[1]}", "r")
        tex = self._update_tex_with_xml(rf.readlines(), xml)
        wf.write(tex)
        rf.close()
        wf.close()
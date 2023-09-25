import subprocess
import xml.etree.ElementTree as ET
from .formats.tex import TEXTemplate
from .generate import customize
from rescon import SCRIPT_DIR

def customize_resume(job_desc, ideo, dtf):
    template = TEXTemplate(dtf, dtf)
    in_xml = template.build()
    ET.indent(in_xml, space="\t")
    out_xml = customize(job_desc, ideo, ET.tostring(in_xml, encoding="utf-8"))
    template.modify(out_xml)
    subprocess.Popen([f"{SCRIPT_DIR}/generate_pdf.sh"])
    return True
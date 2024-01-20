import subprocess
from datetime import datetime
import xml.etree.ElementTree as ET
from .formats.tex import TEXTemplate
from .formats import TEX_DIR
from .generate import customize, answer, create_cl


def customize_resume(job_desc, lines, dtf=None):
    dtf = dtf if dtf else datetime.now().timestamp()
    template = TEXTemplate(dtf)
    in_xml = template.build(lines)
    out_xml = customize(job_desc, ET.tostring(in_xml, encoding="utf-8"))
    template.modify(lines, out_xml)
    subprocess.Popen([f"{TEX_DIR}/generate_pdf.sh", f"{TEX_DIR}/{dtf}.tex", f"{TEX_DIR}/"]).wait()
    return dtf

def create_cover_letter(job_desc, resume):
    return create_cl(job_desc, resume)

def answer_questions(questions, resume):
    questions = "Questions:\n" + "\n".join(questions)
    qas = answer(questions, resume)
    return qas

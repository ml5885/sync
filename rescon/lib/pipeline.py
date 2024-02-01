import subprocess
from datetime import datetime
import ray
import xml.etree.ElementTree as ET
from .formats.tex import TEXTemplate
from .formats import TEX_DIR
from .generate import customize, answer, create_cl
from .model import GPT


def customize_resume(job_desc, lines, api_key, dtf=None):
    dtf = dtf if dtf else datetime.now().timestamp()
    template = TEXTemplate(dtf)
    in_xml = template.build(lines)
    if len(in_xml) <= 0:
        return None, "Invalid resume given. Please refer to documentation for ttx files."
    out_xml = customize(job_desc, ET.tostring(in_xml, encoding="utf-8"), GPT(api_key))
    resume = template.modify(lines, out_xml)
    subprocess.Popen([f"{TEX_DIR}/generate_pdf.sh", f"{TEX_DIR}/{dtf}.tex", f"{TEX_DIR}/"]).wait()
    return dtf, resume

@ray.remote
def create_cover_letter(job_desc, resume, api_key):
    return create_cl(job_desc, resume, GPT(api_key))

@ray.remote
def answer_questions(questions, resume, api_key):
    if not questions:
        return []
    questions = "Questions:\n" + "\n".join(questions)
    qas = answer(questions, resume, GPT(api_key))
    return qas

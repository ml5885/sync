from langchain.schema import (
    SystemMessage,
    AIMessage,
    HumanMessage
)
import openai
import xml.etree.ElementTree as ET
from rescon.lib.model import GPT
from rescon.lib.prompt import *

TOKENS = ["<", ">"]

def _parse_xml(str_xml):
    is_valid = False
    et_xml = None
    try:
        str_xml = str_xml[str_xml.find(TOKENS[0]):str_xml.rfind(TOKENS[1])+1]
        et_xml = ET.fromstring(str_xml)
        is_valid = True
    except Exception as e:
        print(e)
    return is_valid, et_xml

def _parse_tsv(str_tsv, questions):
    li_questions = questions.split("\n")[1:]
    content = str_tsv.split("\n")
    if content[0] == "QUESTION\tANSWER":
        content = content[1:]
    is_valid = len(content) == len(li_questions)
    tsv = None
    if not is_valid: return is_valid, tsv
    try:
        tsv = [{
            "q": c.split("\t")[0],
            "a": c.split("\t")[1]
        } for c in content]
        is_valid = True
    except Exception as e:
        is_valid = False
        print(e)
    return is_valid, tsv


def customize(job_desc, xml, ag):
    data = DATA_RESUME_TEMPLATE.format(job=job_desc, xml_resume=xml)
    log = [SystemMessage(content=SYSTEM_RESUME_TEMPLATE), AIMessage(content=AGENT_RESPONSE), HumanMessage(content=data)]
    is_valid = False
    result = None
    while not is_valid:
        str_response = ag.predict_messages(log)
        is_valid, result = _parse_xml(str_response.content)
    return result

def answer(questions, resume, ag):
    data = DATA_QUESTION_TEMPLATE.format(questions=questions, resume=resume)
    log = [SystemMessage(content=SYSTEM_QUESTION_TEMPLATE), AIMessage(content=AGENT_RESPONSE), HumanMessage(content=data)]
    is_valid = False
    result = None
    while not is_valid:
        str_response = ag.predict_messages(log)
        is_valid, result = _parse_tsv(str_response.content, questions)
    return result

def create_cl(job, resume, ag):
    data = DATA_CL_TEMPLATE.format(job=job, resume=resume)
    log = [SystemMessage(content=SYSTEM_CL_TEMPLATE), AIMessage(content=AGENT_RESPONSE), HumanMessage(content=data)]
    str_response = ag.predict_messages(log)
    return str_response.content

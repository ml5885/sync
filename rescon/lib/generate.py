from langchain.schema import (
    SystemMessage,
    AIMessage,
    HumanMessage
)
import xml.etree.ElementTree as ET
from rescon.lib.model import GPT
from rescon.lib.prompt import *

TOKENS = ["<", ">"]

def _parse_xml(str_xml):
    et_xml = None
    try:
        str_xml = str_xml[str_xml.find(TOKENS[0]):str_xml.rfind(TOKENS[1])+1]
        print(str_xml)
        et_xml = ET.fromstring(str_xml)
    except Exception as e:
        print(e)
    return et_xml

def customize(job_desc, xml, ag=GPT):
    data = DATA_RESUME_TEMPLATE.format(job=job_desc, xml_resume=xml)
    log = [SystemMessage(content=SYSTEM_RESUME_TEMPLATE), AIMessage(content=AGENT_RESPONSE), HumanMessage(content=data)]
    is_valid = False
    result = None
    while not is_valid:
        str_response = ag.predict_messages(log)
        result = _parse_xml(str_response.content)
        if result: is_valid = True
    return result

def answer(questions, resume, ag=GPT):
    data = DATA_QUESTION_TEMPLATE.format(questions=questions, resume=resume)
    log = [SystemMessage(content=SYSTEM_QUESTION_TEMPLATE), AIMessage(content=AGENT_RESPONSE), HumanMessage(content=data)]
    str_response = ag.predict_messages(log)
    return str_response.content

def create_cl(job, resume, ag=GPT):

    pass
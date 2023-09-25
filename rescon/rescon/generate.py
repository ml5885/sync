from langchain.schema import (
    SystemMessage,
    AIMessage,
    HumanMessage
)
import xml.etree.ElementTree as ET
from .model import GPT
from .prompt import (
    SYSTEM_TEMPLATE,
    AGENT_RESPONSE,
    DATA_TEMPLATE
)

def _parse_xml(str_xml):
    et_xml = None
    try:
        et_xml = ET.fromstring(str_xml)
    except Exception as e:
        print(e)
    return et_xml

def customize(job_desc, ideo, xml, ag = GPT):
    data = DATA_TEMPLATE.format(job_description=job_desc, company_ideology=ideo, xml_resume=xml)
    log = [SystemMessage(content=SYSTEM_TEMPLATE), AIMessage(content=AGENT_RESPONSE), HumanMessage(content=data)]
    is_valid = False
    result = None
    while not is_valid:
        str_response = ag.predict_messages(log)
        result = _parse_xml(str_response.content)
        if result: is_valid = True
    return result
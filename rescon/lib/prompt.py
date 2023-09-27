from textwrap import dedent
from langchain.prompts import PromptTemplate

SYSTEM_TEMPLATE = dedent('''\
    I will give you a job description, a company ideology and a resume in an XML format. \
    I want you to change the resume by adding details and changing the wording of the content in the resume so that it appeals to the job description and company ideology. \
    Do not lie about any content. \
    It should be subtle and mainly rely on keywords rather than explicit statements. \
    Keep the exact same LaTex formatting and only change the content provided. \
    Make sure to return the response as an XML in the same format as the resume given. \
    Each tag's content in output XML should be around the same length as the tag's content in the input XML. \
    If you understand this, say "Done".''')

AGENT_RESPONSE = "Done."

DATA_TEMPLATE = PromptTemplate.from_template(
    dedent('''\
        ```description
        {job_description}
        ```

        ```ideology
        {company_ideology}
        ```

        ```xml
        {xml_resume}
        ```\
    ''')
)
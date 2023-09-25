from textwrap import dedent
from langchain.prompts import PromptTemplate

SYSTEM_TEMPLATE = dedent('''\
    I will give you a job description, a company ideology and a resume in an XML format. \
    I want you to change the resume by adding details and changing the wording of each experience, project, and skill on the resume so that it appeals to the job description and company ideology. \
    It should be subtle and mainly rely on keywords rather than explicit statements. \
    Keep the exact same LaTex formatting and only change the content provided. \
    Highlight statistics and accomplishments provided in experiences and projects within the resume when applicable. \
    Make sure to return the response as an XML in the same format as the resume given. \
    Your response should have nothing more than simply the XML with no additional comments on what was changed or any decisions made. 
    Each experience given, project and skills should be around the same length as the input. \
    If you understand this, say "Done".''')

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
from textwrap import dedent
from langchain.prompts import PromptTemplate

SYSTEM_RESUME_TEMPLATE = dedent('''\
    I will give you a job and a resume in an XML format. \
    I want you to change the resume by adding details and changing the wording of the content in the resume so that it appeals to the job. \
    Do not lie too much about any content. \
    It should be subtle and mainly rely on keywords rather than explicit statements. \
    Keep the exact same LaTex formatting and only change the content provided. \
    Make sure to return the response as an XML in the same format as the resume given. \
    Each tag's content in output XML should be around the same length as the tag's content in the input XML. \
    If you understand this, say "Done".''')

SYSTEM_CL_TEMPLATE = dedent('''\
    I will give you a job and a resume. \
    I want you to create a cover letter for the job based on the resume. \
    Do not lie about any content. \
    Do not add any additional formatting details. \
    It should be plain text. \
    If you understand this, say "Done".''')

SYSTEM_QUESTION_TEMPLATE = dedent('''\
    I will give you a set of questions and a resume. \
    I want you to answer the questions even if you have to lie. \
    The returned responses should be in a strict tab-separated format such that it conforms to the following general format:
        QUESTION\tANSWER
        QUESTION_1\tANSWER_1
        ...
        QUESTION_N\tANSWER_N
    If you understand this, say "Done".''')

TEST_TEMPLATE = dedent('''\
    Respond with "Done."''')

AGENT_RESPONSE = "Done."

DATA_RESUME_TEMPLATE = PromptTemplate.from_template(
    dedent('''\
        ```job
        {job}
        ```

        ```xml
        {xml_resume}
        ```\
    ''')
)

DATA_QUESTION_TEMPLATE = PromptTemplate.from_template(
    dedent('''\
        ```questions
        {questions}
        ```
        
        ```resume
        {resume}
        ```\
        QUESTION\tANSWER
    ''')
)

DATA_CL_TEMPLATE = PromptTemplate.from_template(
    dedent('''\
        ```job
        {job}
        ```

        ```resume
        {resume}
        ```\
    ''')
)
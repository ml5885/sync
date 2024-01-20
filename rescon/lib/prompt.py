from textwrap import dedent
from langchain.prompts import PromptTemplate

SYSTEM_RESUME_TEMPLATE = dedent('''\
    I will give you a job and a resume in an XML format. \
    I want you to change the resume by adding details and changing the wording of the content in the resume so that it appeals to the job. \
    Do not lie about any content. \
    It should be subtle and mainly rely on keywords rather than explicit statements. \
    Keep the exact same LaTex formatting and only change the content provided. \
    Make sure to return the response as an XML in the same format as the resume given. \
    Each tag's content in output XML should be around the same length as the tag's content in the input XML. \
    If you understand this, say "Done".''')

SYSTEM_CL_TEMPLATE = dedent('''\
    I will give you a job and a resume. \
    I want you to create a cover letter for the job based on the resume. \
    Do not lie about any content. \
    If you understand this, say "Done".''')

SYSTEM_QUESTION_TEMPLATE = dedent('''\
    I will give you a set of questions and a resume. \
    I want you to answer the questions to the best of your ability given the resume. \
    The returned responses should be in a strict tab-separated format such that it conforms to the following general format:
        QUESTION\tANSWER
        QUESTION_1\tANSWER_1
        ...
        QUESTION_N\tANSWER_N
    Do not lie about any content. \
    If you understand this, say "Done".''')

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
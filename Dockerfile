FROM python:3.10

COPY ./setup.py /setup.py
RUN pip install -e .

WORKDIR /rescon/

RUN curl -sSL https://install.python-poetry.org | POETRY_HOME=/opt/poetry python3 && \
    cd /usr/local/bin && \
    ln -s /opt/poetry/bin/poetry && \
    poetry config virtualenvs.create false

COPY ./pyproject.toml ./poetry.lock* /rescon/

RUN poetry config installer.max-workers 10

ARG INSTALL_DEV=false
RUN bash -c "if [ $INSTALL_DEV == 'true' ] ; then poetry install --no-root ; else poetry install --no-root --no-dev ; fi"

COPY ./rescon /rescon/

ENV PYTHONPATH=/rescon
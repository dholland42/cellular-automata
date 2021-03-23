FROM python:latest

RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -

RUN $HOME/.poetry/bin/poetry config virtualenvs.create false 

COPY . /code

WORKDIR /code/cellular_automata

RUN $HOME/.poetry/bin/poetry install -E serve

ENTRYPOINT ["serve"]

CMD ["--host", "0.0.0.0"]
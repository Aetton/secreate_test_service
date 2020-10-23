FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8


RUN pip install poetry
RUN poetry config virtualenvs.create false
COPY pyproject.toml ./

# for poetry
RUN mkdir -p /app/app/
RUN touch /app/app/__init__.py


RUN poetry install -n


COPY ./app /app/app
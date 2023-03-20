FROM python:3.11-buster

# 
WORKDIR /code

# 
ADD ./pyproject.toml /code/pyproject.toml
ADD ./poetry.lock /code/poetry.lock
ADD ./ecommerce_tcc /code/ecommerce_tcc
ADD ./README.md /code/README.md

ADD ./alembic /code/alembic
ADD ./alembic.ini /code/alembic.ini

# 
RUN pip install --no-cache-dir --upgrade poetry
RUN poetry install --without dev

# 
CMD ["poetry", "run", "uvicorn", "ecommerce_tcc.entrypoints.api:app", "--host", "0.0.0.0", "--port", "8000"]
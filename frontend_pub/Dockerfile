FROM python:3.11-buster

# 
WORKDIR /code

# 
ADD ./pyproject.toml /code/pyproject.toml
ADD ./poetry.lock /code/poetry.lock
ADD ./ecommerce_tcc /code/ecommerce_tcc
ADD ./README.md /code/README.md

# 
RUN pip install --no-cache-dir --upgrade poetry
RUN poetry install --without dev

# 
CMD ["poetry", "run", "gunicorn", "ecommerce_tcc.app:app", "--bind", "0.0.0.0:5000"]
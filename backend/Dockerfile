FROM python:3.10-buster

RUN mkdir app
WORKDIR /app

# ENV PATH="${PATH}:/root/.local/bin"
# ENV PYTHONPATH=${PYTHONPATH}:.

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_NO_INTERACTION=1 \
    PYSETUP_PATH="/opt/pysetup" \
    VENV_PATH="/app/.venv"

ENV PATH="$POETRY_HOME/bin:$VENV_PATH/bin:$PATH"

COPY pyproject.toml .
RUN pip install --upgrade pip
RUN pip install poetry
RUN which pip
RUN which python
RUN python -m poetry install
RUN which uvicorn
# for migrations
# COPY migrations .

COPY . .
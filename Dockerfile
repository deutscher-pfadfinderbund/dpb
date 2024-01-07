FROM python:3.12 as builder

RUN pip install -U poetry==1.7.1

ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=1 \
    POETRY_VIRTUALENVS_CREATE=1 \
    POETRY_CACHE_DIR=/tmp/poetry_cache

WORKDIR /app

COPY pyproject.toml poetry.lock ./

RUN poetry install --without dev --no-directory --compile && rm -rf $POETRY_CACHE_DIR


FROM node:alpine as npm-deps
COPY package.json package-lock.json ./
RUN npm install -g sass && npm install
COPY styles/ ./
RUN sass -I . --style=compressed --no-source-map style.sass:style.css


FROM python:3.12-slim as runtime
WORKDIR /app

ENV VIRTUAL_ENV=/app/.venv \
    PATH="/app/.venv/bin:$PATH"

COPY --from=builder ${VIRTUAL_ENV} ${VIRTUAL_ENV}
COPY --from=npm-deps style.css styles/
COPY --from=npm-deps node_modules node_modules/

COPY . ./

RUN python manage.py collectstatic --noinput && rm -rf node_modules/

EXPOSE 8000

CMD "./run_server.sh"

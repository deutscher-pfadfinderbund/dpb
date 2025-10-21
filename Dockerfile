FROM node:alpine AS npm-deps
# Install npm deps
COPY package.json package-lock.json ./
RUN npm install

# Build CSS
COPY styles/ ./
RUN npx sass -I . --style=compressed style.sass:style.css



FROM python:3.14 AS builder
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

ENV UV_COMPILE_BYTECODE=1\
    UV_LINK_MODE=copy

WORKDIR /app

RUN apt update && apt install -y python3-dev

RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --frozen --group runtime --no-install-project --no-editable


ADD . /app

RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen --no-dev --inexact --no-editable

COPY --from=npm-deps node_modules node_modules/
COPY --from=npm-deps style.css styles/

RUN uv run --frozen python manage.py collectstatic  \
    --noinput  \
    --link \
    --ignore *.map  \
    --ignore *.scss \
    --ignore *.sass \
    && ls static



FROM python:3.14-slim AS runtime
WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1\
    PYTHONUNBUFFERED=1

ENV VIRTUAL_ENV=/app/.venv \
    PATH="/app/.venv/bin:$PATH"

COPY --from=builder --chown=app:app ${VIRTUAL_ENV} ${VIRTUAL_ENV}
COPY --from=builder --chown=app:app /app/static/ static/

COPY . .

EXPOSE 8000

CMD ["./run_server.sh"]

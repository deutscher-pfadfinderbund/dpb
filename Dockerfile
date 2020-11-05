FROM python:3.9-alpine

RUN apk add --no-cache --virtual build-deps python3-dev && \
    pip install -U pipenv pip && \
    apk del build-deps

WORKDIR /code

COPY Pipfile.lock /code/Pipfile.lock

RUN apk add --no-cache --virtual build-deps build-base python3-dev jpeg-dev zlib-dev musl-dev postgresql-dev && \
    pipenv install --system --deploy --ignore-pipfile && \
    apk del build-deps

COPY . /code

EXPOSE 8000

CMD ["pipenv", "run", "gunicorn", "-b", "0.0.0.0:8000", "dpb.wsgi"]
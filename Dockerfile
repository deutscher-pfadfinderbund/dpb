FROM python:3.9-alpine

RUN apk add --no-cache build-base python3-dev py-pip jpeg-dev zlib-dev musl-dev postgresql-dev && \
    pip install -U pipenv pip

WORKDIR /code

COPY Pipfile /code/Pipfile
COPY Pipfile.lock /code/Pipfile.lock

RUN pipenv install --system --deploy --ignore-pipfile

COPY . /code

EXPOSE 8000

CMD ["pipenv", "run", "gunicorn", "-b", "0.0.0.0:8000", "dpb.wsgi"]
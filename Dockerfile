FROM python:3.7-alpine

COPY Pipfile /code/Pipfile
COPY Pipfile.lock /code/Pipfile.lock

WORKDIR /code

RUN apk add --no-cache build-base python-dev py-pip jpeg-dev zlib-dev musl-dev postgresql-dev

RUN pip install -U pipenv pip && \
    pipenv install --system --deploy --ignore-pipfile

COPY . /code

EXPOSE 8000

CMD ["pipenv", "run", "gunicorn", "-b", "0.0.0.0:8000", "dpb.wsgi"]
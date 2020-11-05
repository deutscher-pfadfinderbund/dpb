FROM python:3.9-alpine

# jpeg-dev and zlib-dev are needed by Pillow
RUN apk update && \
    apk add --no-cache --virtual build-deps python3-dev && \
    apk add --no-cache postgresql-libs jpeg-dev zlib-dev && \
    pip install -U pipenv pip && \
    apk del build-deps

WORKDIR /code

COPY Pipfile /code/Pipfile
COPY Pipfile.lock /code/Pipfile.lock

RUN apk --update add --no-cache --virtual build-deps build-base postgresql-dev && \
    pipenv install --system --deploy && \
    apk del build-deps

COPY . /code

EXPOSE 8000

CMD ["pipenv", "run", "gunicorn", "-b", "0.0.0.0:8000", "dpb.wsgi"]
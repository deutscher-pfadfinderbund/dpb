#!/bin/bash

# postgres:16-alpine matches the version docker-compose.yml runs in production.
# Django 6.1 refuses to talk to anything older than PostgreSQL 15.
docker run --name dpbdb -v `pwd`/db/entrypoint:/docker-entrypoint-initdb.d --rm -e POSTGRES_PASSWORD=razupaltuff -e POSTGRES_ROOT_PASSWORD=razupaltuff -e POSTGRES_USER=dpb -e POSTGRES_DB=dpb -p 5432:5432 postgres:16-alpine

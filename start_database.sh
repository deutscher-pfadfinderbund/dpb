#!/bin/bash

docker run --name dpbdb -v `pwd`/db/entrypoint:/docker-entrypoint-initdb.d --rm -e POSTGRES_PASSWORD=razupaltuff -e POSTGRES_ROOT_PASSWORD=razupaltuff -e POSTGRES_USER=dpb -e POSTGRES_DB=dpb -p 5432:5432 postgres:11-alpine

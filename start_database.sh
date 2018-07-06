#!/bin/bash

docker run --name dpbdb -v /home/n2o/Repos/dpb/db/entrypoint:/docker-entrypoint-initdb.d --rm -e POSTGRES_PASSWORD=aFNsEQQC9Gk8NP7urjt4HBegMudJ1zuK -e POSTGRES_ROOT_PASSWORD=aFNsEQQC9Gk8NP7urjt4HBegMudJ1zuK -e POSTGRES_USER=dpb -e POSTGRES_DB=dpb -p 5432:5432 postgres:10-alpine

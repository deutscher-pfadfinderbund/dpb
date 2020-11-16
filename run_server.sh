#!/bin/sh
set -e

apk add --update npm
npm install -g sass
npm install
sass -I . --style=compressed --no-source-map styles/style.sass:styles/style.css
npm uninstall -g sass
apk del npm
python manage.py collectstatic --noinput
rm -rf node_modules

python manage.py migrate --no-input

pipenv run server

#!/bin/sh

apk add --update npm
npm install -g sass
npm install
sass -I . --style=compressed --no-source-map styles/style.sass:styles/style.css
npm uninstall -g sass
apk del npm
python manage.py collectstatic --noinput
rm -rf node_modules

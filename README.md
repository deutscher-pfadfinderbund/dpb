# DPB

[![CircleCI](https://img.shields.io/circleci/project/n2o/dpb.svg?maxAge=2592000)](https://github.com/n2o/dpb)

## Development
This is a Python3 Django project. The requirements are defined in `requirements.txt`. Use a virtualenv for it since this is the best practice.

Assuming `/usr/local/bin/python3` is the path to your python3 binary and `python` is an alias to `python3`:
```bash
$ cd /path/to/this/project
$ mkvirtualenv --python=/usr/local/bin/python3 dpb
$ workon dpb
$ pip install -r requirements.txt
$ python manage.py runserver
```

The server is now accessible under http://localhost:8000

### Create Superuser
Currently, the database is checked in. Since this project is *not* in production mode, this is okay. 

You can add another superuser to the database with:

```bash
$ python manage.py createsuperuser
```

## Requirements for Deployment Server
Started too late to write it down...

### PIL
Before installing PIL via pip, install the following lib:
```bash
$ sudo apt-get install libjpeg-dev
```

If PIL was already installed, reinstall it with:
```bash
$ pip install -I pillow
```

### Bower

Some apps, like `django-scheduler` require Bower. Just install it with:
```bash
$ sudo npm install -g bower
```

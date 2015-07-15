# DPB

Temporarily available at https://christian-meter.de/dpb

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

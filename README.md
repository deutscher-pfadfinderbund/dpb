# Website for DPB

This is a Python3 Django project. 
- The requirements are defined in `pyproject.toml`. 
- Install [uv](https://github.com/astral-sh/uv) for dependency management.

### 1. Start a local database
Start a local database with docker:

```bash
$ docker run -d -p 5432:5432 -e POSTGRES_PASSWORD=razupaltuff -e POSTGRES_USER=dpb -e POSTGRES_DB=dpb postgres:16

# Setup the database schema (only needs to be done once)
$ uv run manage.py migrate
```

### 2. Start the development server

```bash
$ uv run manage.py runserver
```

The server is now accessible under http://localhost:8000

### Create Superuser
Currently, the database is checked in. Since this project is *not* in production mode, this is okay. 

You can add another superuser to the database with:

```bash
$ uv run manage.py createsuperuser
```
# Website for DPB

This is a Python3 Django project. 
- The requirements are defined in `pyproject.toml`. 
- Install [uv](https://github.com/astral-sh/uv) for dependency management.
- Install [npm](https://www.npmjs.com/) for frontend dependencies.
- Install [Docker](https://www.docker.com/) for running a local database.

### 1. Install frontend dependencies

```bash
# Install the npm packages and compile SASS to CSS
# (Bootstrap is customized through SASS; the result lands in dpb/static/styles/)
$ npm install
$ npm run compile-css

# (Optional) Watch SASS files for changes and recompile automatically
$ npm run watch-css
```

### 2. Start a local database
Start a local database with docker:

```bash
$ docker run -d -p 5432:5432 -e POSTGRES_PASSWORD=razupaltuff -e POSTGRES_USER=dpb -e POSTGRES_DB=dpb postgres:16-alpine

# Setup the database schema (only needs to be done once)
$ uv run manage.py migrate
```

At this time the database is empty, so you may want request some initial data from us. 

### 3. Start the development server

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

## Deployment

The site runs from the image published to `ghcr.io/deutscher-pfadfinderbund/dpb`.
`docker compose pull && docker compose up -d` on the server is *not* enough: the
static files will stay as they were.

### Why the assets need a manual step

`collectstatic` runs during the image build, because it needs `node_modules` and
the compiled CSS — neither of which exists in the runtime image. Its output is
baked into `/app/static`. On the server that path is a named volume,
`dpbde_web_static`, which nginx mounts read-only and serves as `/static/`.

Docker copies an image's content into a named volume **only while that volume is
empty**, once, when it is created. Afterwards the volume hides whatever the new
image brought along. A deploy therefore ships new templates against the assets of
whichever build first created the volume. This went unnoticed from February 2024
until September 2026: the markup kept changing, `style.css` did not, and the map
was missing its Leaflet files the whole time.

### After each deploy

```bash
$ cd ~/dpb.de
$ docker compose down
$ docker volume rm dpbde_web_static
$ docker compose up -d
```

Roughly a minute of downtime. Only collected static files live in that volume;
media and the database are bind mounts (`./media`, `./db/data_17`) and are not
touched.

Do **not** reach for `docker compose exec web python manage.py collectstatic`
instead. The runtime image has no `node_modules` and no compiled stylesheet, so
that writes an incomplete set of files into the volume and makes things worse.

### Checking that it worked

```bash
$ curl -sI https://deutscher-pfadfinderbund.de/static/styles/style.css | grep last-modified
```

The date should match the image build, not the previous deploy. Note that the
assets are served with `max-age=86400`, so a browser that has been on the site
before may hold the old stylesheet for up to a day — reload without cache before
concluding anything.

The step above is a workaround. The lasting fix is for the image to keep its
collected assets at a path the volume does not hide and to sync them on start, so
that a deploy carries its own assets.

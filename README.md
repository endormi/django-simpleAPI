# Django-SimpleAPI [![Build Status](https://travis-ci.org/endormi/django-simpleAPI.svg?branch=master)](https://travis-ci.org/endormi/django-simpleAPI) [![Django Version](https://img.shields.io/badge/django-2.1.9-brightgreen.svg?)](https://www.djangoproject.com/download/)  

### Testing with Postman:

Install requirements:

```sh
pip install -r requirements.txt
```

Migrate:

```sh
py manage.py migrate
```

Runserver:

```sh
py manage.py runserver
```

Get all:

```
http://127.0.0.1:8000/movies/
```

By ID:

```
http://127.0.0.1:8000/movies/1
```

### Running locally and adding movies

Install requirements:

```sh
pip install -r requirements.txt
```

Migrate:

```sh
py manage.py migrate
```

Runserver:

```sh
py manage.py runserver
```

Go to this `URL`:

```sh
http://127.0.0.1:8000/movies/
```

There you will see a table with empty inputs where you can add data.

Example of GET `JSON`:

```sh
[
    {
        "id": 1,
        "name": "The Shining",
        "description": "A family heads to an isolated hotel for the winter where a sinister presence influences the father into violence, while his psychic son sees horrific forebodings from both past and future.",
        "category": "Drama, Horror",
        "director": "Stanley Kubrick",
        "based_on": "Stephen King's novel",
        "main_actor": "Jack Nicholson",
        "release_date": "1980-06-13T00:00:00Z"
    }
]
```

#### Using [Curl](https://curl.haxx.se/download.html)

Example response for the HTTP:

```sh
curl -iX GET http://localhost:8000/movies/
```

You should see something like this:

```sh
HTTP/1.0 200 OK
Date: Mon, 25 Feb 2019 ...
Server: WSGIServer/0.2 CPython/3.7.2
Content-Type: application/JSON
etc.
```

> Also you should see details for the movie objects
# Django-SimpleAPI [![Django Version](https://img.shields.io/badge/django-2.1.9-brightgreen.svg?)](https://www.djangoproject.com/download/)  

## Running server

Clone:

```sh
HTTPS: https://github.com/endormi/django-simpleAPI.git or SSH: git@github.com:endormi/django-simpleAPI.git
```

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

Run tests:

```sh
py manage.py test api
```

### Using Postman

> Follow the running server example to get the server up and running.

Get all:

```
http://127.0.0.1:8000/movies/
```

By ID:

```
http://127.0.0.1:8000/movies/1
```

### Using website

> Follow the running server example to get the server up and running.

Go to this `URL`:

```sh
http://127.0.0.1:8000/movies/
```

Example of GET `JSON`:

```sh
[
    {
        "id": 1,
        "name": "The Matrix",
        "description": "A computer hacker learns from mysterious rebels about the true nature of his reality and his role in the war against its controllers.",
        "category": "Action, Sci-Fi",
        "director": "Lana Wachowski, Lilly Wachowski (as The Wachowski Brothers)",
        "main_actor": "Keanu Reeves",
        "release_date": "1999-03-31T00:00:00Z"
    }
]
```

#### Using [Curl](https://curl.haxx.se/download.html)

> Follow the running server example to get the server up and running.

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

[
    {
        "id": 1,
        "name": "The Matrix",
        "description": "A computer hacker learns from mysterious rebels about the true nature of his reality and his role in the war against its controllers.",
        "category": "Action, Sci-Fi",
        "director": "Lana Wachowski, Lilly Wachowski (as The Wachowski Brothers)",
        "main_actor": "Keanu Reeves",
        "release_date": "1999-03-31T00:00:00Z"
    }
]
```

> Also you should see details for the movie objects

It is similar with HTTPIE

#### Using `HTTPIE`

> Follow the running server example to get the server up and running.

Install `HTTPIE`:

```sh
pip install httpie
```

Get the list of movies:

```sh
http http://127.0.0.1:8000/movies/
```

Example response:

```sh
HTTP/1.1 200 OK
...
[
    {
        "id": 1,
        "name": "The Matrix",
        "description": "A computer hacker learns from mysterious rebels about the true nature of his reality and his role in the war against its controllers.",
        "category": "Action, Sci-Fi",
        "director": "Lana Wachowski, Lilly Wachowski (as The Wachowski Brothers)",
        "main_actor": "Keanu Reeves",
        "release_date": "1999-03-31T00:00:00Z"
    }
]
```

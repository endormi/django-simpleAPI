# Django-SimpleAPI [![Build Status](https://travis-ci.org/endormi/django-simpleAPI.svg?branch=master)](https://travis-ci.org/endormi/django-simpleAPI) [![Django Version](https://img.shields.io/badge/django-2.1.9-brightgreen.svg?)](https://www.djangoproject.com/download/)  

### Testing with Postman:

Get all:

```
http://127.0.0.1:8000/movies/
```

By ID:

```
http://127.0.0.1:8000/movies/1
```

### Running locally

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
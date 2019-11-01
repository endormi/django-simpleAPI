from django.db import models


class Movie(models.Model):
    name = models.CharField(max_length=25)
    description = models.CharField(max_length=255)
    category = models.CharField(max_length=50)
    director = models.CharField(max_length=50)
    based_on = models.CharField(max_length=50)
    main_actor = models.CharField(max_length=50)
    release_date = models.DateTimeField(null=True, blank=True)

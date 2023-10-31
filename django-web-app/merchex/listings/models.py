from django.db import models

class Band(models.Model):

    name = models.fields.CharField(max_length=100)


class Title(models.Model):

    titre = models.fields.CharField(max_length=100)
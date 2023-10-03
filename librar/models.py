from django.db import models


class Books(models.Model):
    name = models.CharField(max_length=20)
    Author = models.CharField(max_length=20)

    def __str__(self):
        return f'Название: {self.name},   Автор: {self.Author}'




#from librar.models import Books
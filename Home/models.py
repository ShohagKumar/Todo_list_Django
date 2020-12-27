from django.db import models

# Create your models here.


class Work(models.Model):
    title = models.CharField(max_length=50)
    desc = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.title

# add manually for fetching data  problelm issue
    objects = models.Manager()

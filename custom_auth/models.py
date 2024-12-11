from django.db import models


class Test(models.Model):
    name = models.CharField(max_length=100)
    phone = models.IntegerField()

    def __str__(self):
        return self.name

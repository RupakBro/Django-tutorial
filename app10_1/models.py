from django.db import models


class Person(models.Model):
    full_name = models.CharField(max_length=50)
    contact_address = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    mobile = models.CharField(max_length=50)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return str(self.id)+", "+self.full_name


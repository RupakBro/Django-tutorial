from django.db import models


class Person(models.Model):
    id = models.IntegerField(primary_key=True)
    fullName = models.CharField(max_length=50)
    contactAddress = models.CharField(max_length=50)

    def __str__(self):
        return str(self.id)+", "+self.fullName+", "+self.contactAddress

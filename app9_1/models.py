from django.db import models


class Person(models.Model):
    full_name = models.CharField(max_length=50, help_text="NAME : "),
    contact_address = models.CharField(max_length=50, help_text="ADDRESS : ")

    class Meta:
         ordering = ['-id']

    def __str__(self):
        return str(self.id)+", "+self.full_name+", "+self.contact_address

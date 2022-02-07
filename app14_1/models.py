from django.db import models


class User_Profile(models.Model):
    fullname = models.CharField(max_length=200)
    picture = models.FileField()

    def __str__(self):
        return str(self.id)+", "+self.fullname
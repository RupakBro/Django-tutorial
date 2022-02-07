from django.db import models


class Email(models.Model):
    to=models.CharField(max_length=50)
    subject = models.CharField(max_length=50)
    content = models.CharField(max_length=150)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return str(self.id)+", "+self.to+", "+self.subject
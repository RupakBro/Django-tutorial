from django.db import models

# Create your models here.


class Person2(models.Model):
    full_name = models.CharField(max_length=50, help_text="NAME")
    email_address = models.CharField(max_length=50, help_text="EMAIL")
    comment = models.CharField(max_length=50, help_text="COMMENT")

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return str(self.id)+", "+self.full_name+", "+self.email_address+", "+self.comment
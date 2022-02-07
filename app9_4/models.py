from django.db import models
# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length=130)
    email = models.EmailField(blank=True)
    job_title = models.CharField(max_length=30, blank=True)
    bio = models.TextField(blank=True)

    class Meta:
        ordering = ['-id']
        #db_table = 'app9_3_employee'

    def __str__(self):
        return str(self.id)+", "+self.name+", "+self.email

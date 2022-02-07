from django.db import models


class Employee(models.Model):
    full_name = models.CharField(max_length=50, default='', blank=False)
    contact_address = models.CharField(max_length=50, default='', blank=False)
    mobile = models.CharField(max_length=50, default='', blank=True)
    email = models.EmailField(max_length=50, default='', blank=True)

    class Meta:
        ordering = ['-id']
        #db_table = 'app9_3_employee'

    def __str__(self):
        return str(self.id)+", "+self.full_name+", "+self.contact_address

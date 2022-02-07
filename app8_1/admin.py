from django.contrib import admin
from .models import Person
from .models import Student
from .models import Client

from .models import Place
from .models import Restaurant
from .models import Waiter

from .models import Reporter
from .models import News

from .models import Publication
from .models import Article

# Register your models here.
admin.site.register(Person)
admin.site.register(Student)
admin.site.register(Client)

# One to One

# One to Many
admin.site.register(Reporter)
admin.site.register(News)

# Many to Many
admin.site.register(Publication)
admin.site.register(Article)
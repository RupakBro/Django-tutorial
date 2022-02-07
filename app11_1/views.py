from django.shortcuts import render
from django.http import HttpResponse

from django.contrib.auth.models import User
from django.contrib.auth import authenticate


def index(request):
# Getting All Users
    users = User.objects.all()
    print(users)
    # render on html file
    #return HttpResponse("Hello from app11_1.")

# Creating a New User
    # username
    # password
    # email
    # first_name
    # last_name

    #user1 = User.objects.create_user(username='krishna', password='krishna', email='krishna@gmail.com', first_name='Krishna', last_name = 'Aryal')
    #print(user1.save())

    """
    user2 = User.objects.create_user(username='user1', password='user1')
    user2.email='user1@gmail.com'
    user2.first_name='Kiran'
    user2.last_name='Thapa'
    user2.save()
    """
    #return HttpResponse("Hello from app11_1.")

# Update Password and Delete User
    #user3 = User.objects.get(username='krishna')
    #user3.set_password('Krishna')
    #user3.save()
    #user3.delete()

# Authenticate User
    #user = authenticate(username='admin', password='admin')
    #if user is not None:
    #    print("TRUE")
    #else:
    #    print("FALSE")
    #return HttpResponse("Hello from app11_1.")

# Task
    # Create an application which used to manage users. USER-CRUD Application
        # List all users
        # Filter users
        # Create new user
        # Search user
        # Edit/Update user
        # Delete user

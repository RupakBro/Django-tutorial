from django.shortcuts import render, HttpResponse
from .forms import Profile_Form
from .models import User_Profile

IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg']


def index(request):
    profiles = User_Profile.objects.all()
    print(profiles)
    return  render(request, 'app14_1/index.html', {'profiles': profiles})


def create_profile(request):
    form = Profile_Form()
    if request.method == 'POST':
        form = Profile_Form(request.POST, request.FILES)
        if form.is_valid():
            user_pr = form.save(commit=False)
            user_pr.picture = request.FILES['picture']
            file_type = user_pr.picture.url.split('.')[-1]
            file_type = file_type.lower()
            if file_type not in IMAGE_FILE_TYPES:
                return render(request, 'app14_1/error.html')
            user_pr.save()
            return render(request, 'app14_1/details.html', {'user_pr': user_pr})
    context = {"form": form,}
    return render(request, 'app14_1/create.html', context)
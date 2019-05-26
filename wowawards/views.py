from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import Http404
from .models import Image, Profile
from .forms import NewPostForm
from django.contrib.auth.decorators import login_required
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import ProjectsApi
from .serializer import ProjectSerializer

# Create your views here.
@login_required
def home(request):
    context = {
        'images':Image.objects.all(),
        'profiles': Profile.objects.all()
    }
    return render(request, ('wowawards/base.html'), context)

def profile(request):
    context = {
        'images':Image.objects.all()
    }
    return render(request, ('wowawards/profile.html'), context)

@login_required
def new_post(request):
    current_user=request.user
    if request.method=='POST':
        np_form=NewPostForm(request.POST, request.FILES)
        if np_form.is_valid():
            post=np_form.save(commit=False)
            post.user=current_user
            np_form.save()
            messages.success(request, f'Post Made Successfully!')
        return redirect('wowawards-new-post')
    else:
        np_form=NewPostForm(instance=request.user)
        # p_form=ProfileUpdateForm(instance=request.user.profile)
    context={
        'np_form' : np_form,
    }
    return render(request, 'wowawards/new_post.html', context)

def search_image(request):

    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = user.search_by_image_name(search_term)
        message = f"{search_term}"

        return render(request, 'users/search.html',{"message":message,"images": searched_profiles})

    else:
        message = "You haven't searched for any term"
        return render(request, 'users/search.html',{"message":message})

class ProjectsList(APIView):
    def 


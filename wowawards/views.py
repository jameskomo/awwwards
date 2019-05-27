from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import Http404
from .models import Image, Profile, Ratings
from .forms import NewPostForm
from django.contrib.auth.decorators import login_required
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import ProjectsApi, ProfileApi
from .serializer import ProjectSerializer, ProfileSerializer
from rest_framework import status
from .permissions import IsAdminOrReadOnly
from django.db.models import Avg

# Create your views here.
# @login_required
def home(request):
    context = {
        'images':Image.objects.all(),
        'profiles': Profile.objects.all()
    }
    return render(request, ('wowawards/base.html'), context)

@login_required
def index(request):
    images = Image.objects.order_by('name').annotate(
    avg_design=Avg('ratingsmodel__design'),
    avg_usability=Avg('ratingsmodel__usability'),
    avg_content=Avg('ratingsmodel__content'), 
    )
    context = {'images': images}

    return render(request, 'wowawards/base.html', context)

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
    permission_classes = (IsAdminOrReadOnly,)
    def get(self, request, format=None):
        all_projects=ProjectsApi.objects.all()
        serializers=ProjectSerializer(all_projects, many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializers=ProjectSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


class ProfileList(APIView):
    permission_classes = (IsAdminOrReadOnly,)
    def get(self, request, format=None):
        all_profiles=ProfileApi.objects.all()
        serializers=ProfileSerializer(all_profiles, many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializers=ProfileSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

def search_results(request):

    if 'project' in request.GET and request.GET["project"]:
        search_term = request.GET.get("project")
        searched_projects = Image.search_by_project_title(search_term)
        message = f"{search_term}"

        return render(request, 'wowawards/base.html',{"message":message,"projects": searched_projects})

    else:
        message = "You haven't searched for any term"
        return render(request, 'wowawards/base.html',{"message":message})

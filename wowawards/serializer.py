from rest_framework import serializers
from .models import ProjectsApi
from .models import ProfileApi

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=ProfileApi
        fields=('id','user', 'profile_image', 'bio', 'contact_information')

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model=ProjectsApi
        fields=('id', 'project_title', 'project_description', 'profile', 'pub_date', 'project_image')


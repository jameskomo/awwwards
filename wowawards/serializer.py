from rest_framework import serializers
from .models import ProjectsApi

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model=ProjectsApi
        fields=('project_title', 'project_description', 'profile', 'pub_date', 'project_image ')

     
from rest_framework import serializers
from .models import ProfileApi

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=ProfileApi
        fields=('user', 'profile_image', 'bio', 'projects_posted', 'contact_information')

     
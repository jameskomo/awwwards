from django.db import models
import datetime as dt 
from users.models import Profile
from django.contrib.auth.models import User

# Create your models here.
class Image(models.Model):    
    project_title=models.CharField(max_length=60)
    project_description = models.TextField()
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)
    project_image = models.ImageField(default="default.jpeg", upload_to = 'images/')

    def __str__(self):
        return self.project_title

    def save_project(self):
        self.save()
    
    def delete_project(self):
        Image.objects.filter(id = self.pk).delete() 
    
    def update_project(self, **kwargs):
        self.objects.filter(id = self.pk).update(**kwargs)
    
    def update_project(self, **kwargs):
        self.objects.filter(project_description).update(**kwargs)

    class Meta:
        ordering = ['-pub_date']    

    @classmethod
    def search_profile(cls,search_term):
        profiles = cls.objects.filter(Q(username__username=search_term))
        return profiles
    @classmethod
    def todays_images(cls,date):
        images = cls.objects.filter(pub_date__date = date)
        return images

class ProjectsApi(models.Model):
    project_title=models.CharField(max_length=60)
    project_description = models.TextField()
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)
    project_image = models.ImageField(default="default.jpeg", upload_to = 'images/')


class ProfileApi(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image=models.ImageField(default="profile_pics/default.jpeg", upload_to='profile_pics')
    bio=models.CharField(max_length=200, blank=False)
    # projects_posted=models.ForeignKey(Profile, on_delete=models.CASCADE)
    contact_information = models.TextField()



    


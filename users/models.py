from django.db import models
from django.contrib.auth.models import User



class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image=models.ImageField(default="profile_pics/default.jpeg", upload_to='profile_pics')
    bio=models.CharField(max_length=200, blank=False)
    # projects_posted=models.ForeignKey(Image, on_delete=models.CASCADE)
    contact_information = models.TextField()
    

    def save_profile(self):
        self.save()
    
    def delete_profile(self):
        Image.objects.filter(id = self.pk).delete() 
    
    def update_profile(self, **kwargs):
        self.objects.filter(id = self.pk).update(**kwargs)


class ProfileApi(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image=models.ImageField(default="profile_pics/default.jpeg", upload_to='profile_pics')
    bio=models.CharField(max_length=200, blank=False)
    projects_posted=models.ForeignKey(Profile, on_delete=models.CASCADE)
    contact_information = models.TextField()

    


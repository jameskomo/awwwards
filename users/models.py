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
    project_title=models.CharField(max_length=60)
    project_description = models.TextField()
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    

    def __str__(self):
        return f'{self.user.username} Profile'

class Follow(models.Model):
    username = models.ForeignKey(User, related_name='follower', on_delete=models.CASCADE)
    followed = models.ForeignKey(User, related_name='followed', on_delete=models.CASCADE)
    follow_id = models.CharField(max_length=50,unique=True, null=True)

    def __str__(self):
        return self.follow_id

    def save_like(self):
        self.save()








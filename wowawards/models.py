from django.db import models
import datetime as dt 
from users.models import Profile
from django.contrib.auth.models import User

# Create your models here.
class Image(models.Model):    
    image_name=models.CharField(max_length=60)
    image_caption = models.TextField()
    image_comments = models.TextField()
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)
    photo_image = models.ImageField(default="default.jpeg", upload_to = 'images/')

    def __str__(self):
        return self.image_name

    def save_image(self):
        self.save()
    
    def delete_image(self):
        Image.objects.filter(id = self.pk).delete() 
    
    def update_image(self, **kwargs):
        self.objects.filter(id = self.pk).update(**kwargs)
    
    def update_caption(self, **kwargs):
        self.objects.filter(image_caption).update(**kwargs)

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

class Comment(models.Model):
    comment_content = models.CharField(max_length=300)
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    image = models.ForeignKey(Image,on_delete=models.CASCADE)

    def save_comment(self):
        self.save()

    


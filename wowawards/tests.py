from django.test import TestCase
import datetime as dt
from .models import Image, Profile, Ratings

class ImageTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.project1= Image(project_title='Test', project_description='Test Project Instances', pub_date='May 27, 2019', project_image='media/websites/website1.jpg', project_link='www.google.com')
    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.project1,Image))


    

    # def test_save_method(self):
    #     self.image1.save_image()
    #     images = Image.objects.all()
    #     self.assertTrue(len(images)>0)
        

    def tearDown(self):
        Image.objects.all().delete()
        Profile.objects.all().delete()
        Ratings.objects.all().delete()
    
class ProfileTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.profile1= Profile(profile_image='media/profile_pic/komo2.jpg', bio='here to create')
    def test_instance(self):
        self.assertTrue(isinstance(self.profile1,Profile))

    # def test_save_method(self):
    #     self.image1.save_image()
    #     images = Image.objects.all()
    #     self.assertTrue(len(images)>0)
        

    def tearDown(self):
        Profile.objects.all().delete()

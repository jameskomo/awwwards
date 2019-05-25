from django.test import TestCase
import datetime as dt
from .models import Image, Profile

class ImageTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.image1= Image(image_name = 'Nduma', image_caption ='African Tastes', image_comments ='Food', pub_date ='May 10, 2019, 5:28 p.m.', photo_image='media/images/food.jpg')
    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.image1,Image))

    # def test_save_method(self):
    #     self.image1.save_image()
    #     images = Image.objects.all()
    #     self.assertTrue(len(images)>0)
        

    def tearDown(self):
        Image.objects.all().delete()
        Profile.objects.all().delete()
    
class ProfileTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.profile1= Profile(profile_image='media/images/food.jpg', bio='here to create')
    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.profile1,Profile))

    # def test_save_method(self):
    #     self.image1.save_image()
    #     images = Image.objects.all()
    #     self.assertTrue(len(images)>0)
        

    def tearDown(self):
        Profile.objects.all().delete()

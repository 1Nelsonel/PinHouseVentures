from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    description = models.TextField(max_length=500, blank=True, null=True)
    
    def __str__(self):
        return self.user.username

    @receiver(post_save, sender=User) #add this
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User) #add this
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

class Agent(models.Model):
    name = models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=20, null=True)
    image = models.ImageField(upload_to='agents', null=True)
    email = models.EmailField(null=True)
    description = models.TextField(null=True)
    updated = models.DateTimeField(auto_now=True, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.name[0:50]
    

class Location(models.Model):
    name = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=100, null=True)
    bank = models.CharField(max_length=100, null=True)
    airport = models.CharField(max_length=100, null=True)
    school = models.CharField(max_length=300, null=True)
    mapLink = models.URLField(max_length=2048,null=True)
    updated = models.DateTimeField(auto_now=True, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.name[0:50]

class Propertycategory(models.Model):
    name = models.CharField(max_length=100, null=True)
    updated = models.DateTimeField(auto_now=True, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.name[0:50]

class Property(models.Model):
    title = models.CharField(max_length=100, null=True)
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True)
    size = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    category =models.ForeignKey(Propertycategory,on_delete=models.SET_NULL, null=True)
    bedroom = models.IntegerField(default=0)
    bathroom = models.IntegerField(default=0)
    garage = models.IntegerField(default=0)
    agent = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    rent = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    #images
    imageOne = models.ImageField(upload_to='upload/property_images', null=True, blank=True)
    imageTwo = models.ImageField(upload_to='upload/property_images', null=True, blank=True)
    imageThree = models.ImageField(upload_to='upload/property_images', null=True, blank=True)
    imageFour = models.ImageField(upload_to='upload/property_images', null=True, blank=True)
    imageFive = models.ImageField(upload_to='upload/property_images', null=True, blank=True)
    description = models.TextField(null=True)
    #amenities
    alarm_security =  models.BooleanField(default=False, null=True, blank=True)
    basketball_court =  models.BooleanField(default=False, null=True, blank=True)
    gym =  models.BooleanField(default=False, null=True, blank=True)
    swimming_pool =  models.BooleanField(default=False, null=True, blank=True)
    garden =  models.BooleanField(default=False, null=True, blank=True)
    gated_community =  models.BooleanField(default=False, null=True, blank=True)
    own_compound =  models.BooleanField(default=False, null=True, blank=True)
    #timeline
    updated = models.DateTimeField(auto_now=True, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.title[0:50]

class Blog(models.Model):
    title = models.CharField(max_length=200,null=True, blank=True)
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    image = models.ImageField(upload_to='upload/blog_images', null=True)
    body = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        ordering = ['-updated_at', '-created_at']

    def __str__(self):
        return self.title[0:50]

class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=100,null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    body = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)  

    class Meta:
        ordering = ['-updated_at', '-created_at']

    def __str__(self):
        return self.name[0:50]
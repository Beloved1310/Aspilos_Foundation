from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.


class Contact (models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    subject = models.TextField(max_length=700)
    def __str__(self):
        return self.name

class Join(models.Model):
    uname = models.CharField(max_length=20)
    pnumber = models.CharField(max_length=20)
    uemail = models.EmailField(max_length=20)
    pword = models.CharField(max_length=20)
    
    def __unicode__(self):
        return self.uname


class Post (models.Model):
    subject = models.CharField (max_length=255)
    slug = models.SlugField()
    message = models.TextField()
    name = models.CharField(max_length = 255)
    email = models.EmailField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now_add = True)

    class Meta:
        ordering =  ['created_at']

       
    def __str__(self):
        return self.name + ' | ' + (self.subject)
        







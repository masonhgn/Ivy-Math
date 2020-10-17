from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse



class postAlg(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    clip = models.FileField(upload_to='user_videos/',null=True)
    
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail-alg', kwargs={'pk': self.pk})


class postPrec(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    clip = models.FileField(upload_to='user_videos/',null=True)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail-prec', kwargs={'pk': self.pk})


class postTrig(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    clip = models.FileField(upload_to='user_videos/',null=True)


    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post-detail-trig', kwargs={'pk': self.pk})


class postCalc(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE) 
    clip = models.FileField(upload_to='user_videos/',null=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post-detail-calc', kwargs={'pk': self.pk})



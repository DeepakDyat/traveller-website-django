from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class contact(models.Model):
    name=models.CharField(max_length=90)
    email=models.EmailField()
    phone=models.IntegerField()
    message=models.CharField(max_length=1000)
    def __str__(self):
        return self.email


class package(models.Model):
    package_name=models.CharField(max_length=200)
    package_cate=models.CharField(max_length=200)
    days=models.IntegerField()
    package_image=models.ImageField(upload_to='package_images')
    package_desc=models.CharField(max_length=1000)
    package_price=models.IntegerField()
    pub_date=models.DateTimeField()

    def __str__(self):
        return self.package_name


class booking(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    phone=models.IntegerField()
    city=models.CharField(max_length=200)
    country=models.CharField(max_length=200)



    def __str__(self):
        return self.name

class checkout(models.Model):
    name=models.CharField(max_length=100)
    card_no=models.IntegerField()
    expiry=models.DateField()
    cvv=models.IntegerField()
    def __str__(self):
        return self.name


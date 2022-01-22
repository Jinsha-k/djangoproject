from django.db import models

# Create your models here.
class Signup(models.Model):
	Name=models.CharField(max_length=10)
	Age=models.IntegerField()
	Place=models.CharField(max_length=20)
	Photo=models.ImageField(upload_to='media/',blank=True,null=True)
	Email=models.EmailField(max_length=18)
	Password=models.CharField(max_length=8)

class Gallery(models.Model):
	Photo=models.ImageField()
	Name=models.CharField(max_length=100)
	Price=models.CharField(max_length=100)
	Model=models.CharField(max_length=100)
	Details=models.CharField(max_length=1000)
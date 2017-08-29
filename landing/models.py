from django.db import models

# Create your models here.
'''это таблица в которой мы будем хранить имя и емеил'''
class Profile(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=128) #имя не может быть больше чем 128 символов
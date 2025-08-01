from django.db import models

# Create your models here.
class Users(models.Model):
  name = models.CharField(max_length=255)
  surname = models.CharField(max_length=255)
  phone_number = models.CharField(max_length=50)
  login = models.CharField(max_length=50)
  password = models.CharField(max_length=50)

  def __str__(self):
    return f'{self.name} {self.surname} - {self.phone_number}'
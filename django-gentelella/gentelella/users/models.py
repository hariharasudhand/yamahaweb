from django.db import models
from django.contrib.auth.models import User, Group
from django.dispatch import receiver
from django.db.models.signals import post_save
from PIL import Image


class Departments(models.Model):
    department_name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.department_name}'

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='male_default.png', upload_to='profile_pics')
    phone = models.CharField(max_length=10, blank=True, null=True, default=23213387)
    department = models.IntegerField(default=2)
    group = models.IntegerField(default=2)

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.height >125 or img.width >125:
            output_size = (125, 125)
            img.thumbnail(output_size)
            img.save(self.image.path)


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()

class Group(models.Model):
    group = Group()

    def __str__(self):
        return self.group.name

class GroupPermission(models.Model):
    module = models.CharField(max_length=100, default='Dcn Creation', null=False)
    group = models.CharField(max_length=50, default='2')
    create = models.BooleanField(default=False)
    view = models.BooleanField(default=False)
    update = models.BooleanField(default=False)
    delete = models.BooleanField(default=False)

    def __str__(self):
        return self.groupname
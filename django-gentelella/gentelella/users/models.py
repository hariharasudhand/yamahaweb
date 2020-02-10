from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from PIL import Image


class Departments(models.Model):
    department_name = models.CharField(max_length=100)
    status = models.CharField(max_length=20, default='ACTIVE')

    def __str__(self):
        return f'{self.department_name}'

class Module(models.Model):
    module_name = models.CharField(max_length=100)
    status = models.CharField(max_length=20, default='ACTIVE')
    date_added = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.module_name}'

class Role_Permission(models.Model):
    name = models.CharField(max_length=50, default='')
    create = models.BooleanField(default=False)
    view = models.BooleanField(default=True)
    update = models.BooleanField(default=False)
    delete = models.BooleanField(default=False)
    date_added = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)
    module = models.ForeignKey(Module, on_delete=models.SET_NULL, null=True)
    status = models.CharField(max_length=20, default='ACTIVE')

    def __str__(self):
        return self.name

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "module":
            kwargs["queryset"] = Module.objects.filter(status=['ACTIVE'])
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


class GroupPermission(models.Model):
    name = models.CharField(max_length=25, default='')
    role = models.ForeignKey(Role_Permission, on_delete=models.SET_NULL, null=True)
    status = models.CharField(max_length=20, default='ACTIVE')

    def __str__(self):
        return self.name

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='male_default.png', upload_to='profile_pics')
    phone = models.CharField(max_length=10, blank=True, null=True, default=23213387)
    department = models.ForeignKey('Departments', on_delete=models.SET_NULL, null=True)
    group = models.ForeignKey(GroupPermission, on_delete=models.SET_NULL, null=True)
    status = models.CharField(max_length=20, default='INACTIVE', null=False)

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


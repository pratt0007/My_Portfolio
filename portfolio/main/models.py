from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
# Create your models here.

from ckeditor.fields import RichTextField\


class skill(models.Model):
    name = models.CharField(max_length=20. blank = True, null = true)
    score = models.IntegerField(default= 80 , balnk = True , null = True)
    image = models.FileField(blank = True , null = True , upload_to="skills")
    is_key_skill = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class UserProfile(models.Model):

    user = models.OneToOneField(User , on_delete=models.CASCADE)
    avatar = models.ImageField(blank=true, null = True , upload_to="avatar")
    title = models.CharField(max_length=200, blank=True , null=True)
    bio = models.TextField(blank=true , null=true)
    skills = models.ManyToManyField(skill , blank = True)
    cv = models.FileField(blank=True , null=True  upload_to="cv")

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'
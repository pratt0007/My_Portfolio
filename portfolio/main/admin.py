from django.contrib import admin
from .models import (UserProfile , skill)
# Register your models here.
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('id' , 'user')

@admin.register(skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('id' , 'name' , 'score')


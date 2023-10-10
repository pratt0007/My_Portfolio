from django.contrib import admin
from .models import (UserProfile , skill , Media , certificate, contactprofile  , portfolio)
# Register your models here.
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('id' , 'user')

@admin.register(skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('id' , 'name' , 'score')


@admin.register(Media)
class MediaAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('id','name','is_active')
    readonly_fields = ('slug',)

@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ('id','name')

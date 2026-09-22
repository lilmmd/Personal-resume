from django.contrib import admin
from app_hello.models import Profile, Experience, Education, Project

admin.site.register(Profile)
admin.site.register(Experience)
admin.site.register(Education)
admin.site.register(Project)
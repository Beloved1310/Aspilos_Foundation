from django.contrib import admin

# Register your models here.
from .models import Contact, Join, Post


admin.site.register(Contact),
admin.site.register(Join),
admin.site.register(Post)


from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    search_fields = ['title', 'content']
    list_display=['title','authour','date_posted']
    list_filter=['authour','date_posted']


# Register your models here.
admin.site.register(Post, PostAdmin)

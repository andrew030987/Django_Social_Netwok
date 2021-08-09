from django.contrib import admin

from site_app.models import CustomUser, Post


@admin.register(CustomUser)
class AdminCustomUser(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'about']

@admin.register(Post)
class AdminPost(admin.ModelAdmin):
    list_display = ['author', 'text', 'post_dt']
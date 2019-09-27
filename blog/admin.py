from django.contrib import admin
from .models import Post, UserProfile


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status','created_on', 'beginning_at', 'ending_at')
    list_filter = ("status",)
    search_fields = ['title', 'content', 'beginning_at', 'ending_at']
    prepopulated_fields = {'slug': ('title',)}
    
class UserProfiles(admin.ModelAdmin):
    list_display = ('user', 'location', 'bio', 'birth_date')

admin.site.register(Post, PostAdmin)
admin.site.register(UserProfile, UserProfiles)
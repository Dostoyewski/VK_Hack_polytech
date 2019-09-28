from django.contrib import admin
from .models import Post, UserProfile, Museum, MuseumMember


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status','created_on', 'beginning_at', 'ending_at')
    list_filter = ("status",)
    search_fields = ['title', 'content', 'beginning_at', 'ending_at']
    prepopulated_fields = {'slug': ('title',)}
    
class UserProfiles(admin.ModelAdmin):
    list_display = ('user', 'location', 'bio', 'birth_date')

class MuseumProfiles(admin.ModelAdmin):
    list_display = ('user', 'name', 'description', 'image', 'members', 'slug')
    prepopulated_fields = {'slug': ('name',)}

class ModeratorProfiles(admin.ModelAdmin):
    list_display = ('user', 'museum', 'vorname', 'nachname', 'role', 'image')

admin.site.register(Post, PostAdmin)
admin.site.register(UserProfile, UserProfiles)
admin.site.register(Museum, MuseumProfiles)
admin.site.register(MuseumMember, ModeratorProfiles)
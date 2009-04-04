from django.contrib import admin
from models import Author
from models import Feed
from models import Post
from models import SocialNetwork

# Improve the admin form for Post
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_modified',)
    list_filter = ('title', 'date_modified',)
    ordering = ('-date_modified',)
    search_fields = ('title', 'content',)

admin.site.register(Author)
admin.site.register(Feed)
admin.site.register(Post, PostAdmin)
admin.site.register(SocialNetwork)

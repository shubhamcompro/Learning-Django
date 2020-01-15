from django.contrib import admin
from .models import Post, Tag


# ModelAdmin class is the representation of a model in the admin interface.

# We can place in model also
def display_tags(self):
    return ", ".join(tag.name for tag in self.tags.all()[:])


display_tags.short_description = 'Tags'


class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'title', 'active', display_tags, 'created_at', 'updated_at']
    list_filter = ['active', 'tags']


# admin.site.register(Tag, TagAdmin)
@admin.register(Tag)  # @admin.register(Tag,Post) multiple classes
class TagAdmin(admin.ModelAdmin):
    list_display = ['id']


admin.site.register(Post, PostAdmin)

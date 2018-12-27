from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'pub_date', )
    list_filter = ('title', 'slug', 'pub_date', )
    search_fields = ('title', 'slug', 'pub_date', )
    ordering = ('-pub_date',)


admin.site.register(Post, PostAdmin)

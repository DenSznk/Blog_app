from django.contrib import admin

from blog_application.models import Category, Post, PostCategory


class PostAdmin(admin.ModelAdmin):
    class Meta:
        model = Post

    list_display = (
        'post_header',
        'post_content',
        'post_author',
        'post_tag',
        'post_date_added',

    )
    list_editable = (
        'post_tag',
    )


admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(PostCategory)

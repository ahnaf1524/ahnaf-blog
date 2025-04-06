from django.contrib import admin
from blog.models import Blog, Category, Hashtag
# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    # Define any list display, filters, etc., you want here
    pass

    # Link to the custom CSS file
    class Media:
        css = {
            'all': ('css/custom_blog_admin.css',)  # Path to the custom admin CSS file
        }
admin.site.register(Blog,BlogAdmin)
admin.site.register(Category)
admin.site.register(Hashtag)


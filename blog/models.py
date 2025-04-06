from django.db import models

# A model for Categories (optional)
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

# A model for Hashtags (optional, but more structured than a simple CharField)
class Hashtag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

# Main Blog Model
class Blog(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    title = models.CharField(max_length=255)
    content = models.TextField() 
    author = models.CharField(max_length=13)
    image_url = models.URLField(max_length=500, blank=True, null=True) 
    categories = models.ManyToManyField(Category, blank=True)  
    hashtags = models.ManyToManyField(Hashtag, blank=True) 
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft') 
    published_date = models.DateTimeField(auto_now_add=True) 
    updated_date = models.DateTimeField(auto_now=True)  
    view_count = models.PositiveIntegerField(default=0) 
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title + ' by ' + self. author

    def increase_view_count(self):
        """Increase view count by one."""
        self.view_count += 1
        self.save()


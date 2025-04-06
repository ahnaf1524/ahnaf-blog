from django.shortcuts import render,HttpResponse , get_object_or_404
from blog.models import Blog, Category, Hashtag
from django.core.paginator import Paginator
# Create your views here.
def blogHome(request):
    blogs = Blog.objects.all().order_by('-published_date')
    # Get all categories and hashtags from db
    categories = Category.objects.all()
    hashtags = Hashtag.objects.all()
    # get the filtered values from get request
    selected_hashtage = request.GET.get('hashtag')
    selected_category = request.GET.get('category')
    if(selected_hashtage) :
        blogs = blogs.filter(hashtags__id=selected_hashtage)
    if(selected_category) :
        blogs = blogs.filter(categories__id=selected_category)
    # Pagination
    paginator = Paginator(blogs , 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)   
     # Prepare the context dictionary
    context = {
        'blogs': page_obj,           # List of all blog posts
        'categories': categories, # List of all categories
        'hashtags': hashtags,     # List of all hashtags
    }

    return render(request, 'blog/blog.html' , context)

def blogPost(request , slug):
    blog = get_object_or_404(Blog, slug=slug)
    categories = blog.categories.all()  # Fetch related categories
    hashtags = blog.hashtags.all()      # Fetch related hashtags
    context = {
        'blog': blog,               # The specific blog post object
        'categories': categories,   # Associated categories for the blog post
        'hashtags': hashtags,       # Associated hashtags for the blog post
    }
    return render(request, 'blog/blogPost.html',context)

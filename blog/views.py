from django.shortcuts import render
from blog.models import Post
from django.utils import timezone as tz

# Create your views here.
def post_list(request):
    published = Post.objects.filter(date_published__lte = tz.now()).order_by('date_published')
    r=render(request, 'blog/post_list.html', {'posts': published})
    return r

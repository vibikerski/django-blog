from django.shortcuts import render
from blog.models import Post

def get_all_posts(request):
    posts = Post.objects.all()
    context = {
        "post_list": posts,
    }
    
    return render(
        request,
        'blog/post_template.html',
        context
    )
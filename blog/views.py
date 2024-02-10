from django.shortcuts import render
from blog.models import Post, Author, Comment


def get_all_posts(request):
    posts = Post.objects.all()
    context = {
        "post_list": posts,
    }

    return render(
        request,
        'blog/posts_template.html',
        context
    )


def get_post_by_id(request, post_id):
    post = Post.objects.get(id=post_id)
    comments = Comment.objects.filter(post=post)
    context = {
        "post": post,
        "author": post.author,
        "comments": comments
    }

    return render(
        request,
        'blog/post_template.html',
        context
    )


def get_posts_by_author(request, author_id):
    author = Author.objects.get(id=author_id)
    posts = Post.objects.filter(author=author)

    context = {
        "post_list": posts,
        "author": author,
    }

    return render(
        request,
        'blog/post_by_author_template.html',
        context
    )

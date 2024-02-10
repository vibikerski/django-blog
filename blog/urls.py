from django.urls import path
import blog.views as blog_views

urlpatterns = [
    path("", blog_views.get_all_posts, name="posts"),
    path("post/<int:post_id>", blog_views.get_post_by_id, name="post"),
    path("author/<int:author_id>", blog_views.get_posts_by_author, name="author"),
]

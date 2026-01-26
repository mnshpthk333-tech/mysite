from django.shortcuts import render
from django.template.loader import render_to_string

from django.http import Http404, HttpResponseNotFound

from .models import MyPost

# Create your views here.


def starting_page(request):
    latest_post = MyPost.objects.all().order_by("-date")[:3]

    return render(request, "blog/index.html", {
        "posts": latest_post})


def posts(request):
    all_posts = MyPost.objects.all()
    return render(request, "blog/all-post.html", {
        "all_posts": all_posts
    })


def post_details(request, slug):
    identified_post = MyPost.objects.get(slug=slug)
    return render(request, 'blog/post-detail.html', {
        "post": identified_post,
        "post_tags": identified_post.tags.all()
    })

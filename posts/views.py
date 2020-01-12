from django.shortcuts import render
from .models import Post


def list_view(request):
    # benchmark for 3 posts in db
    return render(request, 'posts/list.html', {
        # 'posts': Post.objects.all(), # 9 queries
        # 'posts': Post.objects.select_related('user'), # 6 queries
        'posts': Post.objects.select_related('user').prefetch_related('tags'),  # 3 queries
        'title': 'Post Title'
    })

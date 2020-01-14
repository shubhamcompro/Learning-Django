from django.shortcuts import render
from .models import Post
from .tasks import create_random_user_accounts

def list_view(request):
    create_random_user_accounts.delay(5)
    # benchmark for 3 posts in db
    return render(request, 'posts/list.html', {
        # 'posts': Post.objects.all(), # 9 queries
        # 'posts': Post.objects.select_related('user'), # 6 queries
        'posts': Post.objects.select_related('user').prefetch_related('tags'),  # 3 queries
        'title': 'Post Title'
    })

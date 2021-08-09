from django.contrib.auth import login
from site_app.models import CustomUser, Post
from django.views import View
from django.shortcuts import render, redirect
from django.views import View

__all__ = [
    'Posts'
]


class Posts(View):
    def get(self, request, user_id):
        if request.user.is_authenticated:
            posts = Post.objects.all()
            user = CustomUser.objects.get(id=user_id)
            return render(request, 'time-line.html', context={'user': user, 'posts': posts})
        return redirect('/')

    def post(self, request, user_id):
        Post.objects.create(
            author=CustomUser.objects.get(id=user_id),
            text=request.POST['text']
        )
        return self.get(request, user_id)
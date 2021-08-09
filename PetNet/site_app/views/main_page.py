from django.shortcuts import render, redirect
from django.views import View
from site_app.models import CustomUser

__all__ = [
    'MainPage',
]


class MainPage(View):
    def get(self, request, user_id):
        if request.user.is_authenticated:
            user = CustomUser.objects.get(id=user_id)
            return render(request, 'personal_info.html', context={'user': user})

        return redirect('/')

from django.contrib.auth import login
from site_app.models import CustomUser
from django.views import View
from django.shortcuts import render, redirect

__all__ = [
    'Registration',
]


class Registration(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return render(request, 'registration.html')
        return redirect('/')

    def post(self, request):
        if request.POST['password'] == request.POST['check_password']:
            user = CustomUser.objects.create(
                username=request.POST['username'],
                first_name=request.POST['first_name'],
                last_name=request.POST['last_name'],
                email=request.POST['email']
            )
            user.set_password(request.POST['password'])
            user.save()
            login(request, user)
            return redirect(f'/user_page/{user.id}')
        return render(request, 'registration.html', context={'error': 'Incorrect data'})

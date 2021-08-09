from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from django.views import View

__all__ = [
    'Login',
    'Logout'
]


class Login(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect(f'/user_page/{request.user.id}')
        return render(request, 'login.html')

    def post(self, request):
        user = authenticate(request,
                            username=request.POST['username'],
                            password=request.POST['password'])
        if user is not None:
            login(request, user)
            return redirect(f'/user_page/{request.user.id}')
        else:
            return render(request, 'login.html', context={'error': 'Incorrect Data'})


class Logout(View):
    def get(self, request):
        logout(request)
        return render(request, 'logout.html')

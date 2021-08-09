from site_app.models import CustomUser
from django.views import View
from django.shortcuts import render, redirect

__all__ = [
    'EditProfile',
]


class EditProfile(View):
    def get(self, request, user_id):
        if request.user.is_authenticated:
            user = CustomUser.objects.get(id=user_id)
            return render(request, 'edit-profile.html', context={'user': user})
        return redirect('/')

    def post(self, request, user_id):
        data = {'first_name': request.POST['firstname'],
                'last_name': request.POST['lastname'],
                'email': request.POST['email'],
                'phone': request.POST['phone'],
                'address': request.POST['address'],
                'about': request.POST['about']}

        CustomUser.objects.filter(id=user_id).update(**data)
        return redirect(f'/user_page/{user_id}')

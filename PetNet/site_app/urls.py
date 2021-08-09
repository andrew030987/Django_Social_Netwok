from django.urls import path
from .views import *


urlpatterns = [
    path('', Login.as_view()),
    path('registration/', Registration.as_view(), name='register'),
    path('user_page/<user_id>', MainPage.as_view(), name='user_page'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('edit-profile/<user_id>', EditProfile.as_view(), name='edit_profile'),
    path('timeline/<user_id>', Posts.as_view(), name='timeline'),
]
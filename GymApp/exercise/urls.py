from django.urls import path
from . import views

urlpatterns = [
    path('', views.home , name='home'),
    path('login', views.login_page, name='login'),
    path('logout', views.logout_user, name='logout'),
    path('registration', views.registration_page, name='registration')
]
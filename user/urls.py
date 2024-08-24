from django.urls import path
from django.urls import re_path
from .import views

app_name = "users"


urlpatterns = [

	path('login/', views.login_user, name='login'),
	path('logout/', views.logout_user, name='logout'),
	path('register/', views.register, name='register'),
]


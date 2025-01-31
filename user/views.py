from django.contrib.auth import authenticate, login
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .forms import LoginUserForm, RegisterUserForm
# Create your views here.
def login_user(request):
	if request.method == 'POST':
		form = LoginUserForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			user = authenticate(request, username=cd['username'], password=cd['password'])
			if user and user.is_active:
				login(request, user)
				return HttpResponseRedirect(reverse('experts:index1'))
	else:
		form = LoginUserForm()
		return render(request, 'users/pages-login.html', {'form': form})

def logout_user(request):
	return HttpResponse("logout")



def register(request):
	if request.method == 'POST':
		form = RegisterUserForm(request.POST)
		if form.is_valid():
			user = form.save(commit=False)
			user.set_password(form.cleaned_data['password'])
			user.save()
			return render(request, 'users/register_done.html')
	else:
		form = RegisterUserForm()
	return render(request, 'users/pages-register.html', {'form': form})
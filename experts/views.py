from django.shortcuts import render
from django.http import HttpResponse


from .models import Expert, News, State, ProjecPar, ExpertsMean


# Create your views here.
def index1(request):
	header_index = State.objects.all()
	return render(request, "index.html", {'header_index': header_index})

def donate(request):
	return render(request, "donate.html")

def expert(request):
	latest_expert_list = Expert.objects.all()
	return render(request, "experts/bisnesExpert.html", {'latest_expert_list': latest_expert_list})


def expert_about(request):
	latest_profile_expert = Expert.objects.order_by('expert_FIO')[:1]
	return render(request, "experts/ExpertsAbout.html", {'latest_profile_expert': latest_profile_expert})

def meropriatia(request):
	latest_meropriatia = News.objects.all()
	return render(request, "News/bisnesMean.html", {'latest_meropriatia': latest_meropriatia})

def expert_mean(request):
	expert_post = ExpertsMean.objects.all()
	return render(request, "News/newsBusines.html", {'expert_post': expert_post})


def profile(request):
	profile_user = Expert.objects.order_by('expert_FIO')[:1]
	profile_post = ExpertsMean.objects.all()

	return render(request, "experts/Lider.html", {'profile_post': profile_post})

def projects(request):
	project_partners = ProjecPar.objects.all()
	return render(request, "projectMV.html", {'project_partners': project_partners})
	
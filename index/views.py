from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth import login,logout,authenticate
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
	return(render(request,'index/index.html'))

def user_login(request):

	if(request.method=="POST"):
		username=request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(username=username,password=password)

		if user:
			if user.is_active:
				login(request)
				return(HttpResponseRedirect(reverse('index')))

			else:
				return HttpResponse('Account Deactivate')
		else:
			return HttpResponse("Invalid User")
	else:
		return(render(request,'index/login.html'))



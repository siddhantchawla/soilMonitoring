from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django import forms
from django.contrib import messages
from django.contrib.auth import authenticate, login

from .forms import *
from .models import *

# Create your views here.
@login_required(login_url='login/')
def index(request):
	
	return render(request, 'index.html', {})

@login_required(login_url='login/')
def dataFill(request):
	if request.method == 'POST':
		form = dataForm(request.POST)
		if form.is_valid():
			userObj = form.cleaned_data
			moisture = userObj['moisture']
			temperature = userObj['temperature']	
			dataform = data.objects.create(user = request.user)
			dataform.temperature = temperature
			dataform.moisture = moisture
			# dataform.time = time.now
			dataform.save()	
			return redirect('dataFill')
		else:
			return render(request, 'datafill.html',{'error': 'Couldnt save the data!', 'form' : form})
             	# return render(request, 'register.html',{'error': 'This Username/Email is not available!', 'form' : form})

	else:
	 	form = dataForm()

	return render(request, 'datafill.html', {'form' : form})
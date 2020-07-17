from django.shortcuts import render,redirect
from .forms import SignUpForm, UserForm, ProfileFrom
from django.contrib.auth import authenticate, login
from .models import Profile
def signup(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username,password=password)
			login(request,user)
			return redirect('/accounts/profile')
	else:
		form = SignUpForm()
	return render(request,'registration/signup.html',{'form':form,})

def profile(request):
	profile = Profile.objects.get(user = request.user)
	return render(request,'accounts/profile.html',{'profile':profile,})

def profile_edit(request):
	profile = Profile.objects.get(user= request.user)
	if request.method == 'POST':
		profile_form = ProfileFrom(request.POST,request.FILES,instance = profile)
		user_form = UserForm(request.POST,instance = request.user)
		if profile_form.is_valid() and user_form.is_valid():
			user_form.save()
			my_profile = profile_form.save(commit = False)
			my_profile.user = request.user
			my_profile.save()
			return redirect('accounts:profile')
	else:
		profile_form = ProfileFrom(instance = profile)
		user_form = UserForm(instance = request.user)
	return render(request,'accounts/profile_edit.html',{'profile_form':profile_form,'user_form':user_form,})
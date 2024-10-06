from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
import random
from django.conf import settings
from django.contrib.auth.views import LoginView
from django.views.decorators.csrf import csrf_exempt
from .forms import UserRegistrationForm
from registration.models import UserProfile

@csrf_exempt
def register(request):
    context = {}
    if settings.UPDATE == True:
        context = {'updating' : 1}
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            # if form.cleaned_data.get('account_type') == settings.SECRET_KEY:
            #     user.is_staff = True
            # elif form.cleaned_data.get('account_type') != user.username:
            #     form = UserRegistrationForm()
            #     return render(request, 'registration/register.html', {'form': form, 'message' : 'Invalid form'})
            user.id = random.randint(100000000000000, 999999999999999)
            user.save()
            # Log the user in
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(request, username=username, password=password)
            profile = UserProfile(user=user)

            profile.member1_name = form.cleaned_data.get('member1_name')
            profile.member1_id = form.cleaned_data.get('member1_id')
            profile.member1_class = form.cleaned_data.get('member1_class')
            profile.member2_name = form.cleaned_data.get('member2_name')
            profile.member2_id = form.cleaned_data.get('member2_id')
            profile.member2_class = form.cleaned_data.get('member2_class')
            profile.member3_name = form.cleaned_data.get('member3_name')
            profile.member3_id = form.cleaned_data.get('member3_id')
            profile.member3_class = form.cleaned_data.get('member3_class')

            profile.save()
            login(request, user)
            # Redirect to home page
            return redirect('home')
    else:
        form = UserRegistrationForm()
    context['form'] = form
    return render(request, 'registration/register.html', context)

@csrf_exempt
def __login(request):
    return LoginView.as_view(template_name='registration/login.html')(request)

@csrf_exempt
def logout_view(request):
    logout(request)
    return redirect('home')
from django.shortcuts import render, get_object_or_404
from ..forms.BabyMarktForms import SignUpForm, LoginForm
from django.http import HttpResponseRedirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from ..models import User, Ad
from django.contrib import messages
def register(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
    else:
        form = SignUpForm()
    return render(request, 'registration/register.html',{"form":form})

def login_user(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(request, username=request.POST["username"], password=request.POST["password"])
            if user is not None:
                login(request, user)
                return HttpResponseRedirect("/")
            else:
                messages.error(request,"Nom d'utilisateur ou mot de passe incorrect")
                return HttpResponseRedirect('/accounts/login/')
    form = LoginForm()
    return render(request, 'registration/login.html', {"form":form})

@login_required
def show_me(request):
    current_user_profile = get_object_or_404(User, pk=request.user.id)
    return render(request, 'babymarkt_app/accounts/user_profile.html', {"current_user":current_user_profile})

@login_required
def show_my_ads(request):
    my_ads = Ad.objects.filter(user_id=request.user.id)
    return render(request, 'babymarkt_app/accounts/my_ads.html', {"my_ads":my_ads})
@login_required
def logout_user(request):
    logout(request)
    return HttpResponseRedirect("/")
from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy


# Create your views here.
def login(request):
    if request.method == "POST":
        print(request.POST)
        #do sth
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        # print(user)
        if user:
            # return HttpResponse("Sucessfully logged in")
            django_login(request, user)
            return redirect(reverse_lazy('polls:index'))
        else:
            return HttpResponse("login failed")
    return render(request, './accounts/login.html')

def logout(request):
    django_logout(request)
    return redirect('accounts:login')


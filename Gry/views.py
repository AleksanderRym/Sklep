from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Gry, Producent, Gatunek
from .forms import CreateUserForm, LoginForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required(login_url='login')
def index(request):
    gatunki = Gatunek.objects.all()
    dane = {'gatunki': gatunki}
    return render(request, 'szablon.html', dane)


@login_required(login_url='login')
def gatunek(request, id):
    gatunek_user = Gatunek.objects.get(pk=id)
    gatunek_gra = Gry.objects.filter(gatunek=gatunek_user)
    gatunki = Gatunek.objects.all()
    dane = {'gatunek_user': gatunek_user,
            'gatunek_gra': gatunek_gra,
            'gatunki': gatunki}
    return render(request, 'gatunek_gra.html', dane)


@login_required(login_url='login')
def gra(request, id):
    gra_user = Gry.objects.get(pk=id)
    gatunki = Gatunek.objects.all()
    dane = {'gra_user': gra_user,
            'gatunki': gatunki}
    return render(request, 'gra.html', dane)


@login_required(login_url='login')
def gra_nazwa(request):
    if request.method == 'GET':
        query = request.GET.get('q')
        gra_nazwa = Gry.objects.filter(nazwa=query).first()
        if gra_nazwa:
            id = gra_nazwa.id
            gra_user = Gry.objects.get(pk=id)
            gatunki = Gatunek.objects.all()
            dane = {'gra_user': gra_user,
                    'gatunki': gatunki}
            return render(request, 'gra.html', dane)
        else:
            gatunki = Gatunek.objects.all()
            error = 'Nie znaleziono gry'
            dane = {'gatunki': gatunki,
                    'error': error}
            return render(request, 'gra.html', dane)


def registerPage(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Konto dla ' + user + ' zostało utworzone.')
                return redirect('login')
    return render(request, 'register.html', {'form': form})


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                if user.is_staff:
                    return redirect('admin/')
                else:
                    return redirect('/')
            else:
                messages.info(request, 'Nazwa lub hasło jest błędne.')
                return render(request, 'login.html', {})
    return render(request, 'login.html', {})


def logoutUser(request):
    logout(request)
    return redirect('login')

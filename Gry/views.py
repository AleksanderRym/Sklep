from django.contrib.auth.models import User
from django.db import IntegrityError
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Gry, Producent, Gatunek, UserGame, UserWishGame
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


@login_required(login_url='login')
def buyGame(request):
    if request.method == 'POST':
        game_id = request.POST['id']
        game = get_object_or_404(Gry, pk=game_id)
        gatunki = Gatunek.objects.all()
        user_has_game = UserGame.objects.filter(user=request.user, game=game).exists()
        if not user_has_game:
            user_game = UserGame.objects.create(user=request.user, game=game)
            user_has_wish_game = UserWishGame.objects.filter(user=request.user, game=game).exists()
            if user_has_wish_game:
                UserWishGame.objects.filter(user=request.user, game=game).delete()
                messages.info(request, 'Kupiono gre i usunięto z listy życzeń.')
                return render(request, 'gra.html', {'gra_user': game, 'gatunki': gatunki})
            else:
                messages.info(request, 'Kupiono gre.')
                return render(request, 'gra.html', {'gra_user': game, 'gatunki': gatunki})
        else:
            messages.info(request, 'Już posiadasz te gre.')
            return render(request, 'gra.html', {'gra_user': game, 'gatunki': gatunki})
    return render(request, 'gra.html', {})


@login_required(login_url='login')
def my_games(request):
    user_games = UserGame.objects.filter(user=request.user)
    games = [user_game.game for user_game in user_games]
    gatunki = Gatunek.objects.all()
    dane = {'games': games,
            'gatunki': gatunki}
    return render(request, 'my_games.html', dane)


@login_required(login_url='login')
def addWishGame(request):
    if request.method == 'POST':
        game_id = request.POST['id']
        game = get_object_or_404(Gry, pk=game_id)
        gatunki = Gatunek.objects.all()
        user_has_game = UserWishGame.objects.filter(user=request.user, game=game).exists()
        if not user_has_game:
            user_has_game = UserGame.objects.filter(user=request.user, game=game).exists()
            if user_has_game:
                messages.info(request, 'Już posiadasz te gre.')
                return render(request, 'gra.html', {'gra_user': game, 'gatunki': gatunki})
            else:
                user_game = UserWishGame.objects.create(user=request.user, game=game)
                messages.info(request, 'Dodano gre do listy życzeń.')
                return render(request, 'gra.html', {'gra_user': game, 'gatunki': gatunki})
        else:
            messages.info(request, 'Gra znajduje się już na liście życzeń.')
            return render(request, 'gra.html', {'gra_user': game, 'gatunki': gatunki})
    return render(request, 'gra.html', {})

@login_required(login_url='login')
def my_wish_games(request):
    user_wish_games = UserWishGame.objects.filter(user=request.user)
    games = [user_game.game for user_game in user_wish_games]
    gatunki = Gatunek.objects.all()
    dane = {'games': games,
            'gatunki': gatunki}
    return render(request, 'my_games.html', dane)
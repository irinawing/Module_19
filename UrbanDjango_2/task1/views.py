#from django.http import HttpResponse
from django.shortcuts import render
from .models import *
from .forms import UserRegister

# Create your views here.
def  platform(requset):
    return render(requset, 'task1/platform.html')


def games(requset):
    games = Game.objects.all()
    context = {'games': games}
    return render(requset, 'task1/games.html', context)


def cart(request):
    title = 'Cart'
    context = {
        'title': title,
    }
    return render(request, 'task1/cart.html', context)

def sign_up(request):
    info = {}
    form = UserRegister(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

            existing_users = Buyer.objects.values_list('name', flat=True)

            if username in existing_users:
                info['error'] = 'Пользователь уже существует'
            elif password != repeat_password:
                info['error'] = 'Пароли не совпадают'
            elif age < 18:
                info['error'] = 'Вы должны быть старше 18'
            else:
                Buyer.objects.create(name=username, age=age, balance=1000)
                info['message'] = f'Приветствуем, {username}!'

        info['form'] = form

    return render(request, 'task1/registration_page.html', info)

    #иной способ
    # def sign_up_by_django(request):
    #     info = {}
    #     form = UserRegister(request.POST or None)
    #
    #     if request.method == 'POST':
    #         if form.is_valid():
    #             username = form.cleaned_data['username']
    #             password = form.cleaned_data['password']
    #             repeat_password = form.cleaned_data['repeat_password']
    #             age = form.cleaned_data['age']
    #
    #             buyers = Buyer.objects.values_list('name', flat=True)
    #
    #             if username in buyers:
    #                 info['error'] = 'Пользователь уже существует'
    #             elif password != repeat_password:
    #                 info['error'] = 'Пароли не совпадают'
    #             elif age < 18:
    #                 info['error'] = 'Вы должны быть старше 18'
    #             else:
    #                 Buyer.objects.create(name=username, age=age, balance=1000)
    #                 info['message'] = f'Приветствуем, {username}!'
    #
    #         info['form'] = form
    #
    #     return render(request, 'task1/registration_page.html', info)



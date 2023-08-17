import uuid

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from telebot import TeleBot
from .models import Report
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from uuid import uuid4
from .models import Token
from datetime import datetime

bot = TeleBot('6547124745:AAHkES88LxUctgqCUuHj13wWxaX98yVrUTc', parse_mode=None)


def index(request):
    try:
        token = Token.objects.get(user = request.user).token_code
    except Exception as ex:
        token = 'not authenticated yet'
        print(ex)
    print(token)
    return render(request, 'main/index.html', {'token': token})


@login_required
def send_msg(request):
    msg = request.POST['input']
    tg_id = Token.objects.get(user = request.user).user_tg_id
    bot.send_message(tg_id, msg)
    report = Report.objects.create(user = request.user, dateandtime = datetime.now(), text = msg)
    return render(request, 'main/index.html', {})


def sign_up(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            token = str(uuid.uuid4())
            user = User.objects.get(username = request.POST['username'])
            token = Token.objects.create(user = user, token_code = request.POST['username'] + token)
            return redirect('login')
        else:
            return render(request, 'registration/sign_up.html', {'form': form})
    if request.method == 'GET':
        form = UserCreationForm()
        return render(request, 'registration/sign_up.html', {'form': form})



from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from API.models import prompt_data, prompt_and_response_data
from .forms import PromptForm

def login(request):
    return render(request, 'login.html', {})

@login_required(login_url='/admin/')
def index(request):
    shelf = prompt_data.objects.all()
    ai_shelf = prompt_and_response_data.objects.all()
    return render(request, 'index.html', {'shelf': shelf, 'ai_shelf': ai_shelf})


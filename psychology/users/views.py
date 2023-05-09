from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, MyLoginForm
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from articles.models import Article
from psychologists.models import Psychologist


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Ваш аккаунт создан: можно войти на сайт.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    user = request.user
    profile = request.user.profile
    context = {'user': user, 'profile': profile}
    return render(request, 'users/profile.html', context)


class MyLoginView(LoginView):
    form_class = MyLoginForm
    template_name = 'users/login.html'
    success_url = reverse_lazy('profile')


def choice(request):
    return render(request, 'users/choice.html')


def home(request):
    articles = Article.objects.all()[:4]
    psy = Psychologist.objects.all()
    # print(articles)
    context = {'articles': articles, 'psychologists': psy}
    return render(request, 'users/home.html', context)

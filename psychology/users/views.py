from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, MyLoginForm, UserUpdateForm
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from articles.models import Article
from psychologists.models import Psychologist, Session, CommentUserPsychologist
from psychologists.forms import SignUpForSession
from django.db.models import Avg


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
    user_id = user.pk
    if user in Psychologist.objects.all():
        sessions = Session.objects.filter(psychologist__in=[user_id])
        average_rating = CommentUserPsychologist.objects.filter(psychologist=user_id).aggregate(Avg('rating'))[
            'rating__avg']
    else:
        sessions = Session.objects.filter(users__in=[user_id])
        average_rating = None
    context = {'user': user, 'profile': profile, 'sessions': sessions, 'av_rate': average_rating}
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


def update_user(request):
    user = request.user
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Перенаправление на страницу профиля или другую нужную страницу
    else:
        form = UserUpdateForm(instance=user)

    context = {'form': form, 'user': user}
    return render(request, 'users/update_user.html', context)


def sign_up_for_session(request, pk):
    psychologist = Psychologist.objects.get(pk=pk)

    if request.method == 'POST':
        form = SignUpForSession(request.POST)
        if form.is_valid():
            session = form.save(commit=False)
            session.psychologist = psychologist
            session.save()
            session.users.add(request.user)
            return redirect('profile')
    else:
        form = SignUpForSession()

    context = {'form': form, 'psychologist': psychologist}
    return render(request, 'users/sign_up_for_session.html', context)
from django.shortcuts import render, redirect
from .models import Psychologist, Session, CommentUserPsychologist
from .forms import PsLoginForm, SessionUpdateForm, RequestUpdateForm, CommentUserPsychologistForm
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.urls import reverse
from django.db.models import Avg



def show_list(request):
    psy = Psychologist.objects.all()
    context = {'psychologists': psy}
    return render(request, 'psychologists/list.html', context)


@login_required
def profile(request):
    profile = request.user.profile
    user = request.user
    context = {'profile': profile, 'user': user}
    return render(request, 'psychologists/profile.html', context)

def psychologist_login(request):
    if request.method == "POST":
        form = PsLoginForm(data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(request, email=email, password=password)
            print(user)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                form.add_error(None, 'Incorrect email or password.')
                print('user error')
        else:
            print('form.errors:', form.errors)
    else:
        form = PsLoginForm()
    return render(request, 'psychologists/login_ps.html', {'form': form})


def psychologist_view(request, pk):
    psy = Psychologist.objects.get(pk=pk)
    average_rating = CommentUserPsychologist.objects.filter(psychologist=pk).aggregate(Avg('rating'))[
        'rating__avg']
    context = {'user': psy, 'av_rate':average_rating}
    return render(request, 'psychologists/psychologist.html', context)


def update_session(request, pk):
    session = Session.objects.get(pk=pk)
    if request.method == 'POST':
        form = SessionUpdateForm(request.POST, instance=session)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Перенаправление на страницу деталей сессии или другую нужную страницу
    else:
        form = SessionUpdateForm(instance=session)

    context = {'form': form, 'session': session}
    return render(request, 'psychologists/update_session.html', context)


def update_request(request, pk):
    session = Session.objects.get(pk=pk)
    if request.method == 'POST':
        form = RequestUpdateForm(request.POST, instance=session)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Перенаправление на страницу профиля или другую нужную страницу
    else:
        form = RequestUpdateForm(instance=session)

    context = {'form': form, 'session': session}
    return render(request, 'psychologists/update_request.html', context)


def list_session(request):
    sessions = Session.objects.filter(Q(is_confirmed=True) & Q(psychologist=request.user.pk))
    context = {'sessions': sessions}
    return render(request, 'psychologists/list_sessions.html', context)


def list_request(request):
    requests = Session.objects.filter(Q(is_confirmed=False) & Q(psychologist=request.user.pk))
    context = {'requests': requests}
    return render(request, 'psychologists/list_requests.html', context)


def session_view(request, pk):
    session = Session.objects.get(pk=pk)
    context = {'session': session}
    return render(request, 'psychologists/session_view.html', context)


def request_view(request, pk):
    requests = Session.objects.get(pk=pk)
    context = {'requests': requests}
    return render(request, 'psychologists/request_view.html', context)


def comment_psychologist_list(request, pk):
    comments = CommentUserPsychologist.objects.filter(psychologist=pk)
    ps = Psychologist.objects.get(pk=pk)
    context = {'comments': comments, 'ps': ps}
    # article_comments_url = reverse('article_comments', kwargs={'pk': pk})
    return render(request, 'psychologists/comments.html', context)


def comment_psychologist(request, pk):
    ps = Psychologist.objects.get(pk=pk)
    if request.method == 'POST':
        form = CommentUserPsychologistForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.psychologist = ps
            comment.save()
            article_url = reverse('psychologist', kwargs={'pk': pk})
            return redirect(article_url)
    else:
        form = CommentUserPsychologistForm()
    context = {'form': form}
    return render(request, 'psychologists/create_comment.html', context)
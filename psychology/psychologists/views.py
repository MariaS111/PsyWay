from django.shortcuts import render, redirect
from .models import Psychologist
from .forms import PsLoginForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy


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

# def show_profile(request, pk):
#     psy = Psychologist.objects.get(pk=pk)
#     context = {'psy': psy}
#     return render(request, 'psychologists/profile.html', context)


# class PsLoginView(LoginView):
#     form_class = PsLoginForm
#     template_name = 'psychologists/login_ps.html'
#     success_url = reverse_lazy('home')


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
    context = {'user': psy}
    return render(request, 'psychologists/psychologist.html', context)
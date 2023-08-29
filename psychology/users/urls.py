from django.urls import path
from django.contrib.auth import views as auth_views
from users.views import MyLoginView, custom_logout
from django.conf import settings
from django.conf.urls.static import static
from users import views as user_views

urlpatterns = [
    path('register/', user_views.register, name='register'),
    path('login/', MyLoginView.as_view(), name='login'),
    path('accounts/profile/update', user_views.update_user, name='update_user'),
    path('logout/', custom_logout, name='logout'),
    ]
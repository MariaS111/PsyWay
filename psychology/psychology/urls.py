from django.contrib import admin
from django.urls import path, include
from users.views import home
from django.conf.urls.static import static
from django.conf import settings
from users import views as user_views
from django.contrib.auth import views as auth_views
from users.views import MyLoginView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', user_views.choice, name='choice'),
    path('accounts/profile/', user_views.profile, name='profile'),
    path('home/', home, name='home'),
    path('users/', include('users.urls')),
    path('articles/', include('articles.urls')),
    path('psychologists/', include('psychologists.urls')),
    path('chats/', include('chats.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

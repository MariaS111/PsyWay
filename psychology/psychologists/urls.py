from django.urls import path
from .views import show_list, psychologist_login, psychologist_view

urlpatterns = [
    path('', show_list, name='list_of_psychologists'),
    path('login/', psychologist_login, name='psy_login'),
    path('<int:pk>/', psychologist_view, name='psychologist'),
]
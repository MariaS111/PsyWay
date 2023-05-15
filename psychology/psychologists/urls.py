from django.urls import path
from .views import show_list, comment_psychologist_list, comment_psychologist, psychologist_login, psychologist_view, update_session, update_request, list_session, list_request, session_view, request_view
from users.views import sign_up_for_session

urlpatterns = [
    path('', show_list, name='list_of_psychologists'),
    path('login/', psychologist_login, name='psy_login'),
    path('<int:pk>/', psychologist_view, name='psychologist'),
    path('<int:pk>/sign_up_for_session', sign_up_for_session, name='sign_up_for_session'),
    path('list_sessions/<int:pk>/', session_view, name='session_view'),
    path('list_requests/<int:pk>/', request_view, name='request_view'),
    path('list_sessions/<int:pk>/update/', update_session, name='session_update'),
    path('list_requests/<int:pk>/update/', update_request, name='request_update'),
    path('list_sessions/', list_session, name='list_session'),
    path('list_requests/', list_request, name='list_request'),
    path('<int:pk>/comments/', comment_psychologist_list, name='psychologist_comments'),
    path('<int:pk>/comments/add_comment/', comment_psychologist, name='psychologist_comment'),
]
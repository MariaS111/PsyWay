from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Chat
from django.db.models import Q


@login_required
def chat_view(request, pk):
    chat = get_object_or_404(Chat, pk=pk)
    context = {'chat': chat}
    return render(request, 'chats/chat.html', context)


@login_required
def chat_list(request):
    user_id = request.user.pk
    chats = Chat.objects.filter(Q(users__in=[user_id]) | Q(psychologists__in=[user_id]))
    context = {'chats': chats}
    return render(request, 'chats/list.html', context)
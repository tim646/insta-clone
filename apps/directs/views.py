from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.utils.decorators import method_decorator

from apps.directs.models import Message, Participant, Chat
from apps.user.models import UserProfile, User
from apps.common.models import Base
from django.views.generic import TemplateView


# Create your views here.

@login_required
def inbox(request, name=None):
    if request.method == 'POST':
        r = request.POST
        chat = r['chat']
        msg = r['msg']
        sender = request.user
        print('chat', chat)
        chat_obj = get_object_or_404(Chat, id=chat)
        Message.objects.create(chat_id=chat, sender=sender, msg=msg)
        return redirect(f'/message/{chat_obj.name}/')
    participants = Participant.objects.filter(~Q(user=request.user), chat__participant__user=request.user)
    context = {
        'participants': participants,
        'all_user': User.objects.all().exclude(id=request.user.id),
    }
    try:
        chat = get_object_or_404(Chat, name=name)
        context['chat'] = chat
        context['partner'] = Participant.objects.filter(chat=chat).exclude(user=request.user).first()
        messages = chat.messages.all().filter(~Q(sender=request.user), is_read=False)
        for message in messages:
            message.is_read = True
            message.save()
    except Exception as e:
        pass
    return render(request, 'directs/direct.html', context)


def create_chat(request, user_id):
    chat = Chat.objects.filter(participant__user=request.user).filter(participant__user__id=user_id).distinct()
    if chat.exists():
        return redirect(f'/message/{chat.first().name}')
    else:
        chat = Chat.objects.create()
        Participant.objects.create(user_id=user_id, chat=chat)
        Participant.objects.create(user=request.user, chat=chat)

        return redirect(f'/message/{chat.name}')

@login_required
def Directs(request, username):
    user = request.user
    messages = Message.get_message(user=user)
    active_direct = username
    directs = Message.objects.filter(user=user, recipient__username=username)
    directs.update(is_read=True)

    for message in messages:
        if message['user'].username == username:
            message['unread'] = 0
    context = {
        'directs': directs,
        'messages': messages,
        'active_direct': active_direct,
    }
    return render(request, 'directs/direct.html', context)


def SendMessage(request):
    from_user = request.user
    to_user_username = request.POST.get('to_user')
    body = request.POST.get('body')

    if request.method == "POST":
        to_user = User.objects.get(username=to_user_username)
        Message.sender_message(from_user, to_user, body)
        return redirect('message')


def UserSearch(request):
    query = request.GET.get('q')
    context = {}
    if query:
        users = User.objects.filter(Q(username__icontains=query) | Q(profile__first_name__icontains=query) | Q(profile__last_name__icontains=query))

        # Paginator
        paginator = Paginator(users, 8)
        page_number = request.GET.get('page')
        users_paginator = paginator.get_page(page_number)

        context = {
            'users': users_paginator,
        }

    return render(request, 'directs/search.html', context)


def NewConversation(request, username):
    from_user = request.user
    body = ''
    try:
        to_user = User.objects.get(username=username)
    except Exception as e:
        return redirect('search-users')
    if from_user != to_user:
        Message.sender_message(from_user, to_user, body)
    return redirect('message')

## socket

@method_decorator(login_required, name='dispatch')
class MessageView(TemplateView):
    template_name = "directs/message.html"

    def get(self, request, *args, **kwargs):

        context = self.get_context_data(**kwargs)
        context['participants'] = Participant.objects.filter(~Q(user=self.request.user),
                                                             chat__participant__user=self.request.user)
        context['all_users'] = UserProfile.objects.all().exclude(id=self.request.user.id)
        try:
            name = kwargs.get('name')
            chat = get_object_or_404(Chat, name=name)
            context['chat'] = chat
            context['partner'] = Participant.objects.filter(chat=chat).exclude(user=self.request.user).first()
            messages = chat.messages.all().filter(~Q(sender=self.request.user), is_read=False)
            for message in messages:
                message.is_read = True
                message.save()
        except Exception as e:
            context['chat'] = Chat.objects.first()
        return self.render_to_response(context)


def create_chat(request, user_id):
    chat = Chat.objects.filter(participant__user=request.user).filter(participant__user__id=user_id).distinct()
    if chat.exists():
        return redirect(f'/message/chat/{chat.first().name}')
    else:
        chat = Chat.objects.create()
        Participant.objects.create(user_id=user_id, chat=chat)
        Participant.objects.create(user=request.user, chat=chat)

        return redirect(f'/message/chat/{chat.name}')

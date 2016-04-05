from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.conf import settings

from chat import models

class LoginView(generic.View):
    def get(self, request):
        return render(request, 'ui/login.html')

    def post(self, request):
        login = request.POST['login']
        request.session['login'] = login
        #return HttpResponseRedirect('/chat')
        return redirect('/chat')


class ChatView(generic.ListView):
    template_name = 'ui/chat.html'
    model = models.ChatMessage
    ordering = 'created_at'
    paginate_by = 50

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        login = self.request.session.setdefault(
            'login', 'N/A'
        )
        context['login'] = login
        context['ws_server_path'] = 'ws://{}:{}/'.format(
            settings.CHAT_WS_SERVER_HOST,
            settings.CHAT_WS_SERVER_PORT,
        )
        return context
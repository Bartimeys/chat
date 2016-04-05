from django.conf.urls import url

from . import views

app_name = 'ui'
urlpatterns = [
    url(r'^$', views.LoginView.as_view(), name='login'),
    url(r'^chat/$', views.ChatView.as_view(), name='chat')
]
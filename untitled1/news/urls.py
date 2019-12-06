from django.conf.urls import url

from . import views

app_name = 'news'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^([0-9]+)/$', views.detail, name='detail'),
    url(r'^register/$', views.RegisterFormView.as_view()),
    url(r'^login/$', views.LoginFormView.as_view()),
    url(r'^logout/$', views.LogoutView.as_view()),
    url(r'^password-change/', views.PasswordChangeView.as_view()),
    url(r'^([0-9]+)/post/$', views.post, name='post'),
    url(r'^([0-9]+)/msg_list/$', views.msg_list, name='msg_list'),

]

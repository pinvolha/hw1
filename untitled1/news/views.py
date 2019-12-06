from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from .models import Post
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.http import HttpResponseRedirect
from django.views.generic.base import View
from django.contrib.auth import logout
from django.contrib.auth.forms import PasswordChangeForm
from .models import Message
from datetime import datetime
from django.http import JsonResponse
import json


app_url = "/news/"


def index(request):
    news = Post.objects.order_by('-published_date')
    context = {
        'news': news,
    }
    return render(request,
                  'index.html', context)


"""def detail(request, post_id):
    post = Post.objects.get(id=post_id)
    details = Post.objects.filter(show=True).get(id=post_id)
    #views = Post.objects.filter(id=post.id).update(count=F('count') + 1)
    context = {
        'post': post,
        'details': details,
            }
    return render(request,
                  'detail.html', context)"""


def detail(request, post_id):
    error_message = None
    if "error_message" in request.GET:
        error_message = request.GET["error_message"]
    return render(request, "detail.html",
        {
            "post": get_object_or_404(Post, pk=post_id),
            "error_message": error_message,
            "latest_messages": Message.objects.filter(chat_id=post_id).order_by('-pub_date')[:5]
        })


class RegisterFormView(FormView):
    form_class = UserCreationForm
    success_url = app_url + "login/"
    template_name = "reg/register.html"

    def form_valid(self, form):
        form.save()
        return super(RegisterFormView, self).form_valid(form)


class LoginFormView(FormView):
    form_class = AuthenticationForm
    template_name = "reg/login.html"
    success_url = app_url

    def form_valid(self, form):
        self.user = form.get_user()
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)


class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(app_url)


class PasswordChangeView(FormView):
    form_class = PasswordChangeForm
    template_name = 'reg/password_change_form.html'
    success_url = app_url + 'login/'

    def get_form_kwargs(self):
        kwargs = super(PasswordChangeView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        if self.request.method == 'POST':
            kwargs['data'] = self.request.POST
        return kwargs

    def form_valid(self, form):
        form.save()
        return super(PasswordChangeView, self).form_valid(form)


def post(request, post_id):
    msg = Message()
    msg.author = request.user
    msg.chat = get_object_or_404(Post, pk=post_id)
    msg.message = request.POST['message']
    msg.pub_date = datetime.now()
    msg.save()
    return HttpResponseRedirect(app_url+str(post_id))


def msg_list(request, post_id):
    res = list(Message.objects.filter(chat_id=post_id).order_by('-pub_date')[:5].values('author__username', 'pub_date', 'message'))
    for r in res:
        r['pub_date'] = \
            r['pub_date'].strftime('%d.%m.%Y %H:%M:%S')
    return JsonResponse(json.dumps(res), safe=False)

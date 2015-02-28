from django.conf.urls import patterns,include,url
from views import CheckEmailStatusAPI,AddEmailToListAPI
from views import SimpleAddEmailToListAPI
from django.views.decorators.csrf import csrf_exempt

urlpatterns = patterns('',
                       url(r'^check/$', CheckEmailStatusAPI.as_view(), name='check_email'),
                       url(r'^add/$', csrf_exempt(SimpleAddEmailToListAPI.as_view()), name='add_email'),
                       )

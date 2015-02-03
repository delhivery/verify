from django.conf.urls import patterns,include,url
from views import CheckEmailStatusAPI,AddEmailToListAPI

urlpatterns = patterns('',
                       url(r'^check/$', CheckEmailStatusAPI.as_view(), name='check_email'),
                       url(r'^add/$', AddEmailToListAPI.as_view(), name='add_email'),
                       )

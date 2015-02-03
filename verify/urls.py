from django.conf.urls import patterns, include, url
from django.contrib import admin
from views import HomeView

urlpatterns = patterns('',
    # Examples:
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^email/', include('SES_emails.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

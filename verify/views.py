__author__ = 'aamir'

from django.views.generic import RedirectView


class HomeView(RedirectView):
    url = 'admin'

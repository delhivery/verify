__author__ = 'aamir'

from models import SuppressedList

class VerifyEmails(object):
    """

    """
    model = SuppressedList
    def _to_set(self, emails=[]):
        """
            converts the returned data list to set object
        :param emails:
        :return:
        """

        email_set = set()
        for email in list(emails):
            email_set.add(email[0])
        return email_set

    def non_blocked_emails(self, emails=[]):
        """
            makes a query to system and returns the list if non blocked emails
        :param email list:
        :return:
        """
        to_return = []
        set().difference()
        blocked_emails =  self.model.objects.filter(email__in=emails, blocked=True).values_list('email')
        if blocked_emails:
            emails_set = self._to_set(blocked_emails)
            return set(emails).difference(emails_set)
        return emails

    def get_emails_status(self, emails=[]):
        """
            makes a query to system and checks the validity of ses_emails
        :param email:
        :return:
        """
        to_return = []
        email_objs = self.model.objects.filter(email__in=emails)
        for obj in email_objs:
            to_return.append(obj.json_response())
        return to_return

    def get_email_obj(self, email):
        """
            makes a query to system and checks the validity of ses_emails
        :param email:
        :return:
        """
        email_obj = self.model.objects.get(email=email)
        return email_obj.json_response()

    def verify(self, emails=[]):
        try:
            if emails:
                return self.non_blocked_emails(emails)
        except ValueError as e:
            raise Exception('Some Error had occurred' + e)

        return emails
from rest_framework.parsers import JSONParser
from rest_framework import renderers
from django.conf import settings

class AWSParser(JSONParser):
    """
    Parses JSON-serialized data.
    """

    media_type = 'test/plain'
    renderer_class = renderers.TemplateHTMLRenderer

    def parse(self, stream, media_type=None, parser_context=None):
        """
        Parses the incoming bytestream as JSON and returns the resulting data.
        """
        parser_context = parser_context or {}
        encoding = parser_context.get('encoding', settings.DEFAULT_CHARSET)

        try:
            data = stream.read().decode(encoding)
            return data
        except ValueError as exc:
            raise Exception('request parse error ')
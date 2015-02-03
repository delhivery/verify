from rest_framework.views import APIView
from rest_framework.response import Response
from models import SuppressedList
from rest_framework import status
from rest_framework.throttling import UserRateThrottle ,AnonRateThrottle
import json


class CheckEmailStatusAPI(APIView):
    """
        This API provides rest implementation to check the status of email blocked by ses
        {"emails": ["examplesr@xyz.in"]}
                        OR
        {"emails": ["examplesr@xyz.in","response":"list"]}
        if "response":"list" is also passed in query system will return the list of valid
        emails only in return blocked emails will be eliminated from the list


    """
    http_method_names = ['post']
    model = SuppressedList
    throttle_classes = (UserRateThrottle,AnonRateThrottle)


    def post(self, request, *args, **kwargs):
        """
            Handles GET requests and instantiates a blank version of the form.
            e.g {
                    "emails":[
                            "me@xyz.com",
                            "you@pqr.com"
                            ],
                    "response": "list"

                    }
        """
        data = request.DATA.copy()
        if data.get('emails', ''):
            if data.get('response', '') == 'list':
                return Response(self.non_blocked_emails(data.get('emails', '')))
            emails = data.get('emails', '')
            obj = self.get_emails_status(emails=emails)
            return Response({'results': obj, 'success': True})
        return Response({'success': False,'error':True,'message':'invalid data', 'data': data})

    def _to_set(self,emails=[]):
        email_set = set()
        for email in list(emails):
            email_set.add(email[0])
        return email_set


    def non_blocked_emails(self,emails=[]):
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
        return []

    def get_emails_status(self, emails=[]):
        """
            makes a query to system and checks the validity of SES_emails
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
            makes a query to system and checks the validity of SES_emails
        :param email:
        :return:
        """
        email_obj = self.model.objects.get(email=email)
        return email_obj.json_response()


class AddEmailToListAPI(APIView):
    """
        This API provides rest endpoint to Add New SES_emails to blocked list
        the input of this API will be the AWS bounce notification JSON
        {
            "notificationType":"Bounce",
            "bounce":{
                        "bounceSubType":"General",
                        "bounceType":"Transient",
                        "reportingMTA":"dsn; a8-58.smtp-out.amazonses.com",
                        "bouncedRecipients":[{
                                        "status":"4.4.7",
                                        "action":"failed",
                                        "diagnosticCode":"smtp; 554 4.4.7 Message expired: unable to deliver in 840 minutes.<421
                                         4.4.2 Connection timed out>",
                                        "emailAddress":"euphrasia.l@getitinfomedia.in"
                                        }],
                        "timestamp":"2015-01-12T19:16:56.392Z",
                        "feedbackId":"0000014adf93d951-9ccbac5d-7f6c-47ce-a089-36596c7eec04-000000",
                    },
            "mail":{
                    "timestamp":"2015-01-12T04:17:09.000Z",
                    "source":"noreply@delhivery.com",
                    "messageId":"0000014adc5c1220-ae6bd30f-d1a3-46cd-afa7-e9903c9997b8-000000",
                    "destination":[
                                    "uma@freeads.in",
                                    "safalta.dwivedi@freeads.in",
                                    "dipika.shah@freeads.in",
                                    "ranjana@freeads.in",
                                    "abhishek.kumar@getit.co.in",
                                    "chandipriya@freeads.in",
                                    "vishwajit.sandal@getit.co.in",
                                    "euphrasia.l@getitinfomedia.in",
                                    "puja.khurana@getitinfomedia.com",
                                    "CODRemittances@delhivery.com"
                    ]},
        }
    """
    http_method_names = ['post']

    def post(self, request, *args, **kwargs):
        """

        :param request:
        :param args:
        :param kwargs:
        :return: Status True/False
        """
        data = request.DATA.copy()

        try:
            if data and data.has_key('bounce'):
                timestamp = data.get('bounce', '').get('timestamp', '')
                bounced_recipients = data.get('bounce', '').get('bouncedRecipients', '')
                if bounced_recipients:
                    for recipient in bounced_recipients:
                        email = recipient.get('emailAddress', '')
                        bounced_email, created = SuppressedList.objects.get_or_create(email=email, blocked_date=timestamp)
                        bounced_email.save()
                    return Response({'success': True, 'error': False}, status = status.HTTP_201_CREATED)
            else:
                to_return = {'error': True, 'msg': 'invalid data', 'data': data}
                return Response(to_return)
        except Exception as e:
            to_return = {'error': True, 'msg': e}
            return Response(to_return)
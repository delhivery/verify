from django.db import models

"""
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


class SuppressedList(models.Model):
    """
        This list maintains the SES_emails which are blocked and needs to verified.
    """
    email = models.EmailField(blank=False, null=False, verbose_name="supressed_email", db_index=True)
    blocked = models.BooleanField(default=True, db_index=True)
    blocked_date = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def json_response(self):
        """

        :rtype : object
        :returns the json object of minimal fields directly
        """
        return {
            'email': self.email,
            'blocked': self.blocked}

    def __unicode__(self):
        return self.email
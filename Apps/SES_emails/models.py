from django.db import models


class SuppressedList(models.Model):
    """
        This list maintains the ses_emails which are blocked and needs to verified.
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


class AWSSubscription(models.Model):
    """
        This will hold the link to subscription of AWS notifications
    """
    data = models.TextField(null=False,blank=False, max_length=2000)
    link = models.URLField(null=False,blank=False,max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.link
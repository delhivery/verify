from django import forms


class VerifyForm(forms.Form):
    """
        Form to check the validity of SES_emails.
    """
    email = forms.EmailField(required=True)
    format = forms.ChoiceField(choices=(('html','html'),('json','json')))

class AddEmailForm(forms.Form):
    """
        Form to add the new email in blocked list.
    """
    json_data = forms.CharField(widget=forms.Textarea())
    # email = forms.EmailField(required=True)
    # blocked_date = forms.DateTimeField(required=False)



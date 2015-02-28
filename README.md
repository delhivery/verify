#Verify Emails 

This app will help in maintaining the list of emails blocked by AWS SNS to prevent further bounce of emails   
##Getting Started

## Installation
    pip install http://pypi.delhivery.com.s3.amazonaws.com/ses_emails-0.2.tar.gz

###OR
    git clone https://github.com/delhivery/verify.git
    cd Apps/SES_emails/
    python setup.py install

#USAGE
### Settings.py
    As this app is using rest frame work you also need to install the django rest framework 
    INSTALLED_APPS = (
        'XXXXXXXXX',
        'XXXXXXXXX',
        'ses_emails',
        'rest_framework',
    )

### Urls.py
    Add the following line in your main urls.py file 
    url(r'^ses_email/', include('ses_emails.urls')),
    
    
###Inside your email send function code
     # VerifyEmails will filter the list and will exclude the blocked emails from list
    to = VerifyEmails().verify(emails=to)

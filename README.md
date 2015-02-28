#Verify Emails 

This app will help in maintaining the list of emails blocked by AWS SNS to prevent further bounce of emails   
##Getting Started

## Installation
    pip install http://pypi.delhivery.com.s3.amazonaws.com/ses_emails-0.2.tar.gz

###OR
    git clone https://github.com/delhivery/verify.git
    cd Apps/SES_emails/
    python setup.py install

##USAGE
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

### DATABASE Sync
    python manage.py syncdb
    
    
### Create and Verify Amazon SES endpoint
    Create an endpoint from AWS notification with eg. XXX.delhivery.com/ses_email/add
    in order to verify that link AWS will send a verification link on the same provided URL, 
    Go to admin panel/AWSSubscription and click that link, once the link is verified AWS will send all the bounced 
    requests JSON data on the same link and this application will take care of rest
     
### Inside your email send function code
     # VerifyEmails will filter the list and will exclude the blocked emails from list
     e.g : to = ['test@test.com','test2@test.com']
    to = VerifyEmails().verify(emails=to) #this will return the Bounced filtered list of emails  

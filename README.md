#Verify Emails 

This app will help in maintaining the list of emails blocked by AWS SNS to prevent further bounce of emails   
##Getting Started

## Installation
Simply add this application inside your codebase and use it

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
        'emails',
        'rest_framework',
    )

### Urls.py
    Add the following line in your main urls.py file 
    url(r'^email/', include('emails.urls')),
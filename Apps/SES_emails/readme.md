# Emails - Delhivery 

This app will help in maintaining the list of emails blocked by ses to prevent further bounce emails   
# Getting Started

## Installation

Simply add this application inside your codebase and


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
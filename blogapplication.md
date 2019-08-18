## In this we are going to create a blog application in which an article will be posted and viewed

***NOTE: DONT TRY TO COPY THE ABOVE CODE AS IS, TRY TO TYPE, SO THAT YOU WILL NOT FACE ANY ISSUES WITH INDENTATION***

#### Steps
First, create a folder say G:\Projects\Django\myblogs. Go to command prompt and navigate to this folder
Once you are at that location, use command prompt and do these steps

1. Create a virtualenvironment with name envblog and install django (mkvirtualenv envblog to create environment 
and pip install django to install django)
2. Create a project called myblogproject (django-admin startproject myblogproject). 
This will create myblogproject/myblogproject/... kind of structure, let us rename top folder as myblog_root 
so the structure is now myblog_root/myblogproject
3. Create an app called myblog with command (python manage.py startapp myblog)
4. Now open the folder in Sublime or VSCode (or any other favorite text editor) 
5. Now go to myblogproject/urls.py and add the entry and also change the import as below

    ```
    from django.contrib import admin
    from django.urls import path

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('', include('myblog.urls')),
    ]
    ```
6. Next create a new file called urls.py in myblog and add the below line for url navigation
    
    ```
    from django.urls import path
    from . import views
    
    urlpatterns = [
        path('', views.home, name='home'),
    ]
    ```
7. Also now go to views.py add the below code

    ```
    from django.shortcuts import render
    from django.http import HttpResponse

    # Create your views here.
    def home(request)
        return HttpResponse('Hello')
    ```

8. Now go to settings.py add the app name in the INSTALLED_APPS
    ```
    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',

        'myblog',
    ]
    ```
9. Now go to command prompt and run the commands
    * ***python manage.py makemigrations***
       If no errors then 
    * ***python manage.py migrate***

10.


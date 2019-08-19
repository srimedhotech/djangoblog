## How to handle Static files?

### What are static files?
* Any static content like images, videos, javascript files (.js), cascading style sheets (.css) are called static file
* More details can be found from here : https://docs.djangoproject.com/en/2.2/howto/static-files/

### What are the steps to handle static files
* Step1 : make sure that you have the entry ***django.contrib.staticfiles*** is 
present in the INSTALLED_APPS section of settings.py 

* Step 2 : Create a folder called ***static*** in ***myblogproject*** so that the files are stored at myblogproject/static

* Step 3 : In settings.py please make sure that STATIC_URL and STATIC_FILE_DIRS are provided with the names. 
    For example we used this in our project myblogproject
    ```
    STATIC_URL = '/static/'
    
    #add this
    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, 'myblogproject/static/'),
    ]
    ```
* Step 4 : Now create one more folder called css inside the myblogproject/static/css. Now create one more file with name base.css
* Step 5: Open base.html and cut all the content within the <style>  </style> tags and paste it in base.css and save
* Step 6: Now we need to link this base.css in the base.html, we can do so by adding the following in the <head>
    ```
    <head>
    ....
    
    <link rel="stylesheet" href="{% static 'css/base.css' %}">
    
    ```
    To load the static content, wherever you want to use put the below statement
    {% load static %} and then use that static keyword as used above ***href="{% static 'css/base.css' %}">***
* Step 6 : That's it, refresh now and check. It works as earlier

**Note: you can link other content to the images, videos, link by using the ***{% static ....%}***

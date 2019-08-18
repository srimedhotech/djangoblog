# django blog project
##To describe Generic views

###Introduction
## Generic Views 
(Ref: from Django official Documentation) https://docs.djangoproject.com/en/2.2/topics/class-based-views/generic-display/

Writing Web applications can be monotonous, because we repeat certain patterns again and again. Django tries to take away some of that monotony at the model and template layers, but Web developers also experience this boredom at the view level.

Django’s generic views were developed to ease that pain. They take certain common idioms and patterns found in view development and abstract them so that you can quickly write common views of data without having to write too much code.

We can recognize certain common tasks, like displaying a list of objects, and write code that displays a list of any object. Then the model in question can be passed as an extra argument to the URLconf.

Django ships with generic views to do the following:

* Display list and detail pages for a single object. If we were creating an application to manage conferences then a TalkListView and a RegisteredUserListView would be examples of list views. A single talk page is an example of what we call a “detail” view.
* Present date-based objects in year/month/day archive pages, associated detail, and “latest” pages.
* Allow users to create, update, and delete objects – with or without authorization.
Taken together, these views provide easy interfaces to perform the most common tasks developers encounter.



#### Views are two types
1. Function based views - which we already know that we write the view as function
2. Class based views - These views are based on the class, rather than functions. You can write you own class based views or make use of the ones that are already provided by Django. 
3. A view is a callable which takes a request and returns a response. This can be more than just a function, and Django provides an example of some classes which can be used as views. These allow you to structure your views and reuse code by harnessing inheritance and mixins. These views are contained in django.views.generic 

4. The different types of views are 
    * TemplateView
    * RedirectView
    * ListView
    * DetailView
    * FormView...
    ...more info can be found from the official Django documentation at
    https://docs.djangoproject.com/en/2.2/ref/class-based-views/
    
5. The way we use these views is to inherit from an existing view and override attributes or methods (such as get_context_data) in your subclass to provide new values or methods. Then we just need to add this new view into our URLconf. As these views are class based, and not a function, so we point the URL to the ***as_view()*** class method instead, which provides a function-like entry to class-based views
Let us see an exmaple below for TemplateView

    #1 - Step is to inherit
    ```
    # some_app/views.py
    from django.views.generic import TemplateView

    class AboutView(TemplateView):
        template_name = "about.html"

    ```
    #2 Ref this as_view in the urls.py
    ```
    # urls.py
    from django.urls import path
    from some_app.views import AboutView

    urlpatterns = [
        path('about/', AboutView.as_view()),
    ]
    
    ```
### Another Example is ListViews (To Display certain list of items)
    
    ```
    # models.py
    
    from django.db import models
    class Publisher(models.Model):
      name = models.CharField(max_length=30)
      address = models.CharField(max_length=50)    
    ```
Next, we need to define a view:

    ```
    # views.py
    from django.views.generic import ListView
    from books.models import Publisher

    class PublisherList(ListView):
        model = Publisher
    ```
Finally hook that view into your urls:
    
    ```
    # urls.py
    from django.urls import path
    from books.views import PublisherList

    urlpatterns = [
        path('publishers/', PublisherList.as_view()),
    ]
    ```
This template will be rendered against a context containing a variable called object_list that contains all the publisher objects. A very simple template might look like the following:

In the template, add this code to view the list.
   ```
    {% extends "base.html" %}
    {% block content %}
        <h2>Publishers</h2>
        <ul>
            {% for publisher in object_list %}
                <li>{{ publisher.name }}</li>
            {% endfor %}
        </ul>
    {% endblock %}
    ```




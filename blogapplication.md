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

10. Now Let us run the server and check if we are getting the Hello text (python manage.py runserver)and open http://127.0.0.1:8000
11. Now we need to create a model to hold our blog information
12. Our blog information is stored in a class named Article which will have the title, content and status (active or not)
13. Now go to models.py and add the below code
    ```
    class Article(models.Model):
        title = models.CharField(max_length=120)
        content = models.TextField()
        active = models.BooleanField(default=True)
    ```

14. Next step is to create a base.html in the myblogproject. Create a folder called templates within myblogproject and create new file called base.html. So the structure should now look like myblogproject/templates/base.html
15. Now go to settings.py and in the DIRS of TEMPLATES add 'myblogproject/templates' path. After adding it should look like this.
    'DIRS': [os.path.join(BASE_DIR, 'myblogproject/templates') ],
16. Open base.html add the below code
    ```
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta http-equiv="X-UA-Compatible" content="ie=edge">
        <title>Welcome</title>
    </head>
    <body>
        <h1>Welcome to my blog world</h1>
        {% block content %}

        {% endblock %}
    </body>
    </html>
    ```
17. Now go to myblog/views.py and modify the content of home function as below
    ```
    def home(request):
        render (request, 'base.html', {})
    ```
18.  Now I modify the ***base.html*** content add little bit of css and menu

    ```
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta http-equiv="X-UA-Compatible" content="ie=edge">
        <title>Welcome</title>
        <style>
            #topmenu li{
                display: inline-block;
                width: 120px;
                text-decoration: none;
                text-align: center;
                margin-left: 20px;
                padding: 5px;
                background-color: #117;
            }

            #topmenu li a{
                text-decoration: none;
                color: white
            }
            .centerIt{
                text-align: center
            }
            body{
                background-color: #1c7cdd;
                font-size: 20px;
                color: white;;
            }
            .inactive{
                color: rgb(170, 152, 152);
                text-decoration: line-through;
                width : 150px;
            }
        </style>

    </head>
    <body>
        <h1 class="centerIt">Welcome to my blog world</h1>
        <div id="topmenu" class="centerIt">
            <ul>
                <li><a href="/">Home</a></li>
                <li><a href="/articles/">Blogs</a></li>
                <li><a href="/add/">Add Blog</a></li>
            </ul>
        </div>
        {% block content %}

        {% endblock %}
    </body>
    </html>
    
    ```

19. Now you see 3 menu items ***(Home, Blogs and Add Blog)***
20. First let us implement add blog functionality to add the blog (or Article) to the database
21. Create a new file called ***forms.py in myblog/***
22. Open the forms.py and let us add a class with name ***BlogForm*** inherited from ***forms.ModelForm***. See below
    ```
    from django import forms
    from .models import Article

    class BlogForm(forms.ModelForm):

        class Meta:
            model = Article
            fields = '__all__'
    ```
    what we are doing here is telling the class which model it has to refer for the fields and to consider all fields (as shown in meta)
23. Now go to myblogproject/urls.py to add the below entry in the urlpatterns
    ***path('articles/', include('myblog.urls')),***
24. Now go to myblog/urls.py and add the below entry in the urlpatterns
    ***path('add/', views.addarticle, name='add_article'),***
25. The above steps to ensure that when we click on the link ***"add blog"***, we get navigated to 'http://127.0.0.1/articles/add'
26. Next natural step is to handle this request in the views.py. Let us switch now to views.py add a function with name "add". Please note that we need to have a template to show the form to add the article.
27. So now go to myblog and add a folder with name 'templates' and inside that create one more folder with name 'articles'
28. Now create a file called ***add_article.html*** and add the content
    ```
    {% extends 'base.html' %}
    {% block content %}
    <h1>Add a Blog</h1>

    <form method="POST">
        {% csrf_token %}
        {{ form.as_p}}
        <button type="submit">Add Blog</button>
    </form>

    {% if messages %}
    <ul class="messages">
        {% for message in messages %}
        <li>{{ message }}</li>
        {% endfor %}
    </ul>
    {% endif %}

    {% endblock %}
    ```
29. What we did above step is created a form and added a button. The messages are displayed using messages feature of Django
30. Now open views.py add the below code
    ```
    def addarticle(request):
        if request.method == "POST":
            form = BlogForm(request.POST)
            if form.is_valid():
                art = form.save(commit=False)
                art.save()
                messages.info(request, "Your article {} is submitted successfully".format(art.title))
                return redirect('/') #we will change to later to '/articles/'
            else:
                messages.info(request, "Error")
                return redirect( "/")
        else:
            form = BlogForm()
            return render(request, 'articles/add_article.html',  { 'form': form })
    
    ```
31. Now go to the URL http://127.0.0.1:8000 and click on the link ***'Add Blog'***
32. You should be able to see the form to fill the article
33. I have made some style related changes to myblog/add_article.html and you can replace the entire content with the one below
    ```
    {% extends 'base.html' %}

    {% block content %}
        <div class="centerIt">
            <h1 >Add a Blog</h1>

        <form method="POST">
            {% csrf_token %}
            {{ form.as_p}}
            <button type="submit">Add Blog</button>
        </form>

        {% if messages %}
        <ul class="messages">
            {% for message in messages %}
            <li>{{ message }}</li>
            {% endfor %}
        </ul>
        </div>
        {% endif %}

    {% endblock %}
    ```
34. Now it is time to show the blog added as a list at one place. To achieve this first add a template in myblog/templates with name article_list.html
35. Add the below content in the artile_list.html. In this we show the active blogs with hyperlink and the inactive ones as normal text.
    ```
    {% extends 'base.html' %}
    {% block content %}

    <h1>Full List of Articles</h1>
    <ul>
    {% for item in object_list %}
        {% if item.active %}
        <li><a href="/articles/{{item.id}}">{{ item.title}}</a> </li>
        {% else %}
        <li class='inactive'><a href="/articles/{{item.id}}">{{ item.title}}</a></li>
        {% endif %}
    {% endfor %}
    </ul>
    {% endblock %}
    ```
36. To display the list, now we will make use of the ListView from generic Views
37. Go to myblog/views.py add the below code
    ```
    #At the top add these lines
    from django.shortcuts import render, redirect, get_object_or_404
    from .forms import BlogForm
    from django.contrib import messages

    from django.views.generic import (
        ListView,
    )

    from .models import Article

    #step2 - Create a class derived from ListView
    #within the class, we need to have the template name and queryset i.e. 
    #from where we need to get the list of objects.
    class ArticleListView (ListView):
        template_name = 'articles/article_list.html'
        queryset = Article.objects.all()
    
    #This function is called whenever the listview is called.
    
    def get_context_data(self, **kwargs):
        context = super(ArticleListView, self).get_context_data(**kwargs)
        return context
    ```
38. Now we need to make use of this newly created list view
39. To achieve this, we will go to urls.py and ensure we have the below code
    ```    
    from django.urls import path
    from . import views
    from . views import ArticleListView
    #app_name = 'articles'

    urlpatterns = [
        #replace the original path('', views.home, name= 'home') with
        path('', ArticleListView.as_view(), name = 'article-list'),
        
        path('add/', views.addarticle, name='add_article'),
    ]
    ```
40. Again in the myblog/views.py add the below code
    ```
    #when the form is valid and success message is shown 
    #change the line 
    #return redirect('/') to     return redirect('/articles/')
    
    ```
41. That's it, now if you submit a new article, you can see the list of articles in the page http://127.0.0.1:8000/articles. Also you can navigate directly to the URL to see the list of articles (blogs)

42. Next Step is to handle the click event on the blogs where we can show the details of each article (blog)
43. We will achieve this by using another in-built view called ***"DetailView"***
44. To do this, let us make the changes 
    * Create a template
    * Create a class derived from DetailView
    * Make an entry in the myblog/urls.py and use the class derived from DetailView
    * Handle the url navigation in the myblog/views.py

45. Go to the folder myblog/templates/articles add a new file called ***article_detail.html***

    ```
    {% extends 'base.html' %}

    {% block content %}
        <div class="centerIt">
        <h1>Your Article Information details</h1>
        <hr>
        <h2>{{ object.title}}</h2>
        {% if object.active %}
        <p>Status: Active</p>
        {% else %}
        <p>Status: Not Active</p>
        {% endif %}
        <p>{{ object.content}}></p>
        </div>
    {% endblock %}
    ```
    The ***object*** that is used above is taken from the class inhertied from detail view 
    
 46. Now go to ***myblog/views.py*** 
      ```
     At the top import DetailView as well
     from django.views.generic import (
        ListView,
        DetailView #newly added
     )
    #Add this class derived from DetailView
    class ArticleDetailView (DetailView):
        template_name = 'articles/article_detail.html'
        model = Article

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Article, id=id_)
        
    ```
    
47. Now go to myblogs/urls.py - import the ArticleDetailView and modify path
    Step1 : from .views import ArticleListView, ***ArticleDetailView*** 
    Step2 :  ***path('<int:id>', ArticleDetailView.as_view(), name = 'article-detail'),***
    
48. That's it. Now navigate to http://127.0.0.1:8000/articles and select the one with link, you will see the URL as
http://127.0.0.1:8000/articles/1 or http://127.0.0.1:8000/articles/5 like that. Now you will see the details of the article/blog

### Admin related changes
1. open myblog/admin.py
2. Import the model by adding this line of code ***from myblog.models import Article***
3. Register your model by adding this line of code ***admin.site.register(Article)***
4. Now navigate to http://127.0.0.1:8000/admin and from the backend also you can add new articles
5. You can make some of them inactive and observed the deactivated one is striked off.

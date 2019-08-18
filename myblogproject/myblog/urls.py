from django.urls import path
from . import views
from .views import ArticleListView, ArticleDetailView
#app_name = 'articles'

urlpatterns = [
    path('', ArticleListView.as_view(), name = 'article-list'),
    path('<int:id>', ArticleDetailView.as_view(), name = 'article-detail'),
    path('add/', views.addarticle, name='add_article'),

]
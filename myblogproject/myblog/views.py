from django.shortcuts import render, redirect, get_object_or_404
from .forms import BlogForm
from django.contrib import messages
from django.views.generic import (
    ListView,
    DetailView
 )

from .models import Article

# Create your views here.
def home(request):
    return render(request, 'base.html', {})

def addarticle(request):
    if request.method == "POST":
        form = BlogForm(request.POST)
        if form.is_valid():
            art = form.save(commit=False)
            art.save()
            messages.info(request, "Your article {} is submitted successfully".format(art.title))
            return redirect('/articles/')
        else:
            messages.info(request, "Error")
            return redirect( "/")
    else:
        form = BlogForm()
        return render(request, 'articles/add_article.html',  { 'form': form })

#####-------------------------------------------------------#####
class ArticleListView (ListView):
    template_name = 'articles/article_list.html'
    queryset = Article.objects.all()
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super(ArticleListView, self).get_context_data(**kwargs)
        return context

#####-------------------------------------------------------#####
#                           Article Details                     #
#####-------------------------------------------------------#####
class ArticleDetailView (DetailView):
    template_name = 'articles/article_detail.html'
    model = Article

    def get_object(self):
        id_ = self.kwargs.get("id") 
        return get_object_or_404(Article, id=id_)
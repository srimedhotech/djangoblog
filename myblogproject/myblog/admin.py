from django.contrib import admin

# Register your models here.
from myblog.models import Article

admin.site.register(Article)
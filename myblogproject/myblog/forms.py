from django import forms

from .models import Article

class BlogForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = '__all__'
        widgets = {
          'content': forms.Textarea(attrs={'rows':20, 'cols':80}),
          'title' : forms.TextInput(attrs={'size': '84'}),
        }
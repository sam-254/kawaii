from django import forms
from .models import Category



class NewsForm(forms.Form):
    title = forms.CharField(max_length=150, label='Title :',
     widget=forms.TextInput(attrs=
        {"class": 'form-control'}
    ))
    content = forms.CharField(label = 'Text ', required=False,
     widget=forms.Textarea(attrs=
        {
            "class": 'form-control',
            "rows": 5
        }))
    is_published = forms.BooleanField(label='Is published :', initial=True)
    category = forms.ModelChoiceField(queryset=Category.objects.all(),
     empty_label='Select a Category', widget=forms.Select(attrs=
        {"class": 'form-control mb-3'
        }))

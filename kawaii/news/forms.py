from django import forms
# from .models import Category
from .models import News



# class NewsForm(forms.Form):
    # title = forms.CharField(max_length=150, label='Title :',
    #  widget=forms.TextInput(attrs=
    #     {"class": 'form-control'}
    # ))
    # content = forms.CharField(label = 'Text ', required=False,
    #  widget=forms.Textarea(attrs=
    #     {
    #         "class": 'form-control',
    #         "rows": 5
    #     }))
    # is_published = forms.BooleanField(label='Is published :', initial=True)
    # category = forms.ModelChoiceField(queryset=Category.objects.all(),
    #  empty_label='Select a Category', widget=forms.Select(attrs=
    #     {"class": 'form-control mb-3'
    #     }))


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        # fields = '__all__'
        fields = ['title', 'content', 'is_published', 'category', 'photo', ]
        widgets = {
            'title': forms.TextInput(attrs={"class": 'form-control'}),
            'content': forms.Textarea(attrs={"class": 'form-control',"rows": 5}),
            'category': forms.Select(attrs={"class": 'form-control mb-3'}),
            'photo': forms.FileInput(attrs={"class": 'form-control mb-3',
                                            "enctype": "multipart/form-data"
            })
        }
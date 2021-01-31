from django.shortcuts import render, get_object_or_404, redirect
from django.core.files.storage import FileSystemStorage


from .models import News, Category
from .forms import NewsForm


def index(request):
    news = News.objects.all()
    context = {
        'news': news,
        'title': 'News list',
        }
    return render(request, 'news/index.html',context=context)


def get_category(request, category_id):
    current_category_news = News.objects.filter(category_id=category_id)
    # current_category = Category.objects.get(pk=category_id)
    current_category = get_object_or_404(Category, pk=category_id)


    return render(request, 'news/category.html', {
        'current_category_news': current_category_news,
        'current_category': current_category})


def view_news(request, news_id: int):
    # current_news = News.objects.get(pk=news_id)
    current_news = get_object_or_404(News, pk=news_id)
    return render(request,  'news/view_news.html', {'current_news': current_news})


def add_news(request):
    if request.method == "POST":
       
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            # news = News.objects.create(**form.cleaned_data)         #without model connected
            news = form.save()
            return redirect(news)
    else:
        form = NewsForm()

    return render(request, 'news/add_news.html', {
        "form": form
    })
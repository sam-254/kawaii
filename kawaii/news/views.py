from django.shortcuts import render
from django.http import HttpResponse

from .models import News, Category

def index(request):
    news = News.objects.all()
    categories = Category.objects.all()
    context = {
        'news': news,
        'title': 'News list',
        'categories': categories
        }
    return render(request, 'news/index.html',context=context)


def get_category(request, category_id):
    current_category_news = News.objects.filter(category_id=category_id)
    categories = Category.objects.all()
    current_category = Category.objects.get(pk=category_id)

    return render(request, 'news/category.html', {
        'current_category_news': current_category_news,
        'categories': categories,
        'current_category': current_category})
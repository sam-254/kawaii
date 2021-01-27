from django.shortcuts import render, get_object_or_404

from .models import News, Category

def index(request):
    news = News.objects.all()
    context = {
        'news': news,
        'title': 'News list',
        # 'categories': categories
        }
    return render(request, 'news/index.html',context=context)


def get_category(request, category_id):
    current_category_news = News.objects.filter(category_id=category_id)
    # current_category = Category.objects.get(pk=category_id)
    current_category = get_object_or_404(Category, pk=category_id)


    return render(request, 'news/category.html', {
        'current_category_news': current_category_news,
        # 'categories': categories,
        'current_category': current_category})


def view_news(request, news_id: int):
    # current_news = News.objects.get(pk=news_id)
    current_news = get_object_or_404(News, pk=news_id)
    return render(request,  'news/view_news.html', {'current_news': current_news})
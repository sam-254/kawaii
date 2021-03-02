from django.shortcuts import render, get_object_or_404, redirect
from django.core.files.storage import FileSystemStorage
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy

from .models import News, Category
from .forms import NewsForm
from .helper import error_404_view


class HomeNews(ListView):
    model = News
    template_name = 'news/home_news_list.html'
    context_object_name = 'news'
    paginate_by = 3

    # this line below is alternative version of adding method in queryset
    # queryset = News.objects.select_related('category')

    # extra_context = {'title': 'Home'}


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Home | Kawaii'
        return context

    def get_queryset(self):
        # select_related added for lazy loading queries to sql (optimizing) |
        # passed "category" because related model is category
        return News.objects.filter(is_published=True).select_related('category')



class NewsByCategory(ListView):
    model = News
    template_name = 'news/category.html'
    context_object_name = 'current_category_news'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(pk=self.kwargs['category_id'])
        return context


    def get_queryset(self):
        return News.objects.filter(category_id=self.kwargs['category_id']).select_related('category')

    # def get_queryset(self):
    #     # first variant for getting all news of current category
    #     # current_category = Category.objects.get(pk=self.kwargs['category_id'])
    #     # return current_category.get_news.all()
    #     # first variant end
    #     return Category.objects.filter(category_id=self.kwargs['category_id'])


class ViewNews(DetailView):
    model = News

    context_object_name = 'current_news'

    # template_name = 'news/news_detail.html'

    # pk_url_kwarg = 'news_id'


class CreateNews(CreateView):
    form_class = NewsForm
    template_name = 'news/add_news.html'
    # success_url = reverse_lazy('news')


# def index(request):
#     news = News.objects.all()
#     context = {
#         'news': news,
#         'title': 'News list',
#         }
#     return render(request, 'news/index.html', context=context)


# def get_category(request, category_id):
#     current_category_news = News.objects.filter(category_id=category_id)
#     # current_category = Category.objects.get(pk=category_id)
#     current_category = get_object_or_404(Category, pk=category_id)


    # return render(request, 'news/category.html', {
    #     'current_category_news': current_category_news,
    #     'current_category': current_category})


# def view_news(request, news_id: int):
#     # current_news = News.objects.get(pk=news_id)
#     current_news = get_object_or_404(News, pk=news_id)
#     return render(request,  'news/view_news.html', {'current_news': current_news})


# def add_news(request):
#     if request.method == "POST":

#         form = NewsForm(request.POST, request.FILES)
#         if form.is_valid():
#             # news = News.objects.create(**form.cleaned_data)         #without model connected
#             news = form.save()
#             return redirect(news)
#     else:
#         form = NewsForm()

#     return render(request, 'news/add_news.html', {
#         "form": form
#     })

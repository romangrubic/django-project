from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import News
from .forms import NewsForm


# Create your views here.
def get_news(request):
    """Create a view that will return a list of post and
    render them to the blogposts.html template"""
    news_list = News.objects.filter().order_by('-published_date')
    paginator = Paginator(news_list, 8)
    page = request.GET.get('page')
    try:
        news = paginator.page(page)
    except PageNotAnInteger:
        news = paginator.page(1)
    except EmptyPage:
        news = paginator.page(paginator.num_pages)
    return render(request, "newsblog.html", {'news': news})


def news_detail(request, pk):
    """Create a view that returns a single Post object
    based on the post ID (pk) and render it  to the
    'postdetail.html' template. Or return a 404 error if
    the post is not found """
    news = get_object_or_404(News, pk=pk)
    news.views += 1
    news.save()
    return render(request, "newsdetail.html", {'news': news})


def create_or_edit_news(request, pk=None):
    """Create a view that allows us to create or edit
    a news depending if the news ID is null or not"""
    news = get_object_or_404(News, pk=pk) if pk else None
    if request.method == "POST":
        form = NewsForm(request.POST, request.FILES, instance=news)
        if form.is_valid():
            news = form.save()
            return redirect(news_detail, news.pk)
    else:
        form = NewsForm(instance=news)
    return render(request, 'newsform.html', {'form': form})


def get_news_news(request):
    """Create a view that will return a list of new with tag: news and
    render them to the blogposts.html template"""
    news_list = News.objects.filter(tag='N')
    paginator = Paginator(news_list, 8)
    page = request.GET.get('page')
    try:
        news = paginator.page(page)
    except PageNotAnInteger:
        news = paginator.page(1)
    except EmptyPage:
        news = paginator.page(paginator.num_pages)
    return render(request, "newsblog.html", {'news': news})


def get_news_federation(request):
    """Create a view that will return a list of new with tag: update and
    render them to the blogposts.html template"""
    news_list = News.objects.filter(tag='F')
    paginator = Paginator(news_list, 8)
    page = request.GET.get('page')
    try:
        news = paginator.page(page)
    except PageNotAnInteger:
        news = paginator.page(1)
    except EmptyPage:
        news = paginator.page(paginator.num_pages)
    return render(request, "newsblog.html", {'news': news})

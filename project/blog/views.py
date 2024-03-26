from django.contrib.auth import login, logout
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ArticleForm, LoginForm, RegistrationForm
from .models import *


def index(request):
    categories = Category.objects.all()
    articles = Article.objects.all()
    sort_field = request.GET.get('sort')

    if sort_field:
        articles = articles.order_by(sort_field)

    context = {
        'title': 'Blog Page',
        'categories': categories,
        'articles': articles
    }

    return render(request, 'blog/index.html', context)


def category_page(request, category_id):
    categories = Category.objects.all()
    articles = Article.objects.filter(category_id=category_id)
    category = Category.objects.get(pk=category_id)
    sort_field = request.GET.get('sort')

    if sort_field:
        articles = articles.order_by(sort_field)

    context = {
        'title': f"Категория: {category.title}",
        'categories': categories,
        'articles': articles
    }

    return render(request, 'blog/index.html', context)


def article_detail(request, article_id):
    article = Article.objects.get(pk=article_id)
    article.views += 1
    article.save()
    articles = Article.objects.all()
    articles = articles.order_by('-views')

    context = {
        'article': article,
        'articles': articles[:4]
    }

    return render(request, 'blog/article_detail.html', context)


def add_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = Article.objects.create(**form.cleaned_data)
            article.save()
            return redirect('article', article.pk)
    else:
        form = ArticleForm()

        context = {
            'form': form,
            'title': 'Добавить статью'
        }

        return render(request, 'blog/article_form.html', context)


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if user:
                login(request, user)
                return redirect('index')
            else:
                return redirect('login')
        else:
            return redirect('login')
    else:
        form = LoginForm()

    context = {
        'form': form,
        'title': 'Авторизация'
    }

    return render(request, 'blog/user_login.html', context)


def user_logout(request):
    logout(request)
    return redirect('login')


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            return redirect(login)
        else:
            return redirect('register')
    else:
        form = RegistrationForm()

    context = {
        'form': form,
        'title': 'Регистрация'
    }

    return render(request, 'blog/register.html', context)


def search_results(request):
    word = request.GET.get('q')
    articles = Article.objects.filter(
        Q(title__icontains=word) | Q(content__icontains=word)
    )
    context = {
        'articles': articles
    }

    return render(request, 'blog/index.html', context)


def delete_article(request, id):
    article = Article.objects.get(id=id)
    if request.method == 'POST':
        article.delete()
        return redirect('index')
    context = {
        'article': article
    }
    return render(request, 'blog/confirm_delete.html', context)
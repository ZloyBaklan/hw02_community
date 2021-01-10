from django.shortcuts import render, get_object_or_404
from .models import Post, Group


def index(request):
    '''
    Сортировка по "свежести" постов
    '''
    latest = Post.objects.order_by("-pub_date")[:11]
    return render(request, "index.html", {"posts": latest})


def group_posts(request, slug):
    '''
    Функция get_object_or_404 получает по заданным критериям объект из
    базы данных или возвращает сообщение об ошибке, если объект не найден.
    '''
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.all().order_by("-pub_date")[:12]
    return render(request, "group.html", {"group": group, "posts": posts})

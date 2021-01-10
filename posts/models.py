from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Group(models.Model):
    '''
    Заголовок,
    ссылка,
    описание.
    '''
    title = models.CharField(max_length=200, null=False)
    slug = models.SlugField(unique=True)
    description = models.TextField(max_length=300)
    '''
    Возврат понятного отображения заголовка в панель администрирования
    '''
    def __str__(self):
        return self.title


class Post(models.Model):
    '''
    Основной текст поста,
    дата публикации,
    автор,
    возможность ссылаться на группу.
    '''
    text = models.TextField()
    pub_date = models.DateTimeField("date published", auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name="post_author")
    '''
    Чтобы пост не пропал при удалении группы задаем SET_NULL
    '''
    group = models.ForeignKey(Group, on_delete=models.SET_NULL,
                              related_name="posts", blank=True, null=True)

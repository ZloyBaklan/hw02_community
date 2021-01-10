from django.contrib import admin
'''
Из файла models импортируем модели Post,  Group
'''
from .models import Post, Group


class PostAdmin(admin.ModelAdmin):
    '''
    Перечисляем поля, которые должны отображаться в "админке",
    добавляем интерфейс для поиска по тексту постов,
    добавляем возможность фильтрации по дате.
    '''
    list_display = ("pk", "text", "pub_date", "author",)
    search_fields = ("text",)
    list_filter = ("pub_date",)
    '''
    Данное свойство сработает для всех колонок:
    где пусто - там будет эта строка
    '''
    empty_value_display = "-пусто-"


'''
При регистрации Post источником конфигурации для неё назначен класс PostAdmin
'''
admin.site.register(Post, PostAdmin)


class GroupAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ("pk", "title", "description", "slug",)
    search_fields = ("title", "description",)
    list_filter = ("title",)
    empty_value_display = "-пусто-"


admin.site.register(Group, GroupAdmin)

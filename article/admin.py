from django.contrib import admin

# Register your models here.


from .models import Article, Author, Poll, Question


admin.site.register(Article)
admin.site.register(Author)
admin.site.register(Poll)
admin.site.register(Question)
from django.contrib import admin

# Register your models here.


from .models import Article, Author, Poll, Question, Choice

class ChoiceInline(admin.TabularInline):
    """Choice objects can be edited inline in the Question editor."""
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    """Definition of the Question editor."""
    fieldsets = [
        (None, {'fields': ['title']}),
        ('type of question', {'fields': ['typeQ',]}),
        ('question', {'fields': ['description',]}),
        # ('polls', {'fields': ['polls']}), 
        
    ]
    
    inlines = [ChoiceInline]
    list_display = ('title', )
    
    search_fields = ['title']
   

class PollAdmin(admin.ModelAdmin):
    # formfield_overrides = {
    #     models.ManyToManyField: {'widget': RichTextEditorWidget},
    # }
    """Definition of the Poll editor."""
    fieldsets = [
        (None, {'fields': ['title']}),
        ('Date information', {'fields': ['timeOfBegin',]}),
        ('Questions', {'fields': ['questions',]}),
    ]
    
    list_display = ('title', 'timeOfBegin')
    list_filter = ['timeOfBegin']
    search_fields = ['title']
    date_hierarchy = 'timeOfBegin'




admin.site.register(Article)
admin.site.register(Author)
admin.site.register(Poll, PollAdmin)
admin.site.register(Question, QuestionAdmin)
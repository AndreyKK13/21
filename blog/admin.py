from django.contrib import admin
from blog.models import Post, Comment, Quiz, Question, Answer

# Register your models here.

admin.site.register(Post)
admin.site.register(Comment)

class QuestionInLine(admin.TabularInline):
    model = Question
class QiuzAdmin(admin.ModelAdmin):
    inlines = (QuestionInLine,)

admin.site.register(Quiz, QiuzAdmin)
admin.site.register(Question)
admin.site.register(Answer)

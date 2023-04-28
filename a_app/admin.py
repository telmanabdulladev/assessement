from django.contrib import admin
from a_app.models import Exam, Account, Question, Forum, Comment, Resource, Answer, Result, UserAnswerCard

# Register your models here.

admin.site.register(Exam)
admin.site.register(Account)
admin.site.register(Question)
admin.site.register(Forum)
admin.site.register(Resource)
admin.site.register(Comment)
admin.site.register(Answer)
admin.site.register(Result)
admin.site.register(UserAnswerCard)

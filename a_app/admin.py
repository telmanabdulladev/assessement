from django.contrib import admin
from a_app.models import Exam, Account, Question, Form, Comment, Resource

# Register your models here.

admin.site.register(Exam)
admin.site.register(Account)
admin.site.register(Question)
admin.site.register(Form)
admin.site.register(Resource)
admin.site.register(Comment)

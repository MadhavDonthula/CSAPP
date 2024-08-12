from django.contrib import admin

from .models import Assignment, QuestionAnswer

admin.site.register(Assignment)
admin.site.register(QuestionAnswer)
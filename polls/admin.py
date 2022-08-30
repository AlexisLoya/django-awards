from django.contrib import admin
from .models import Question, Choice


# Register your ssss here.
class ChoiceInLine(admin.StackedInline):
    """Add Choices when you add questions"""
    model = Choice
    extra = 2


class QuestionAdmin(admin.ModelAdmin):
    """P"""
    fields = ["pub_date", "question_text"]
    inlines = [ChoiceInLine]
    list_display = ("question_text","pub_date","was_published_recently")
    list_filter = ["pub_date"]
    search_fields = ["question_text"]


admin.site.register(Question, QuestionAdmin)

from django.contrib import admin
from .models import Question, Post
from django.db import models
from martor.widgets import AdminMartorWidget

class YourModelAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': AdminMartorWidget},
    }

# Register your models here.
admin.site.register(Question)
admin.site.register(Post, YourModelAdmin)

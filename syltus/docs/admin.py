from django.contrib import admin
from .models import *
from martor.widgets import AdminMartorWidget
# Register your models here.

class ArticleInline(admin.StackedInline):
    model = Article.attachment.through
    extra = 1
    verbose_name="附件"
    verbose_name_plural = verbose_name

class ArticleAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields":["title", "issue", "col", "author", "description"]}),
        ("正文", {"fields":["content"]}),
        ("附加文本", {"fields":["key"]}),
        (None, {"fields":["pub_date"]})
    ]
    formfield_overrides = {
        models.TextField: {'widget': AdminMartorWidget},
    }
    inlines = [ArticleInline]

admin.site.register(Categoty)
admin.site.register(Issue)
admin.site.register(Column)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Attach)
admin.AdminSite.site_header = "SyltusDocs Nova 管理"
admin.AdminSite.site_title = "SyltusDocs Nova [Beta]"
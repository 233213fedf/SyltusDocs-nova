from django.db import models
from django.utils import timezone
from martor.models import MartorField

"""
=============================================================
    docs/models.py
    SyltusDocs Nova: 数据库模型定义

    (C)SyltusWorks 2024
=============================================================
"""

# Create your models here.
class Categoty(models.Model): # 书刊大板块
    title = models.CharField("名称",max_length=200)
    description = models.TextField("描述",max_length=200)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "类目"
        verbose_name_plural = verbose_name

class Issue(models.Model): # 分期信息
    cat = models.ForeignKey(Categoty, on_delete=models.CASCADE, verbose_name="所属")
    
    year = models.IntegerField("年份")
    number = models.IntegerField("期次")
    def __str__(self):
        return str(self.year)+"第"+str(self.number)+"期 / "+self.cat.title
    class Meta:
        verbose_name = "分册"
        verbose_name_plural = verbose_name

class Column(models.Model):
    title = models.CharField("名称",max_length=200)
    cat = models.ForeignKey(Categoty, on_delete=models.CASCADE, verbose_name="所属")
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "板块"
        verbose_name_plural = verbose_name

class Article(models.Model):
    col = models.ForeignKey(Column, on_delete=models.CASCADE, verbose_name="板块")
    # cat = models.ForeignKey(Categoty, on_delete=models.CASCADE, verbose_name="所属")
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE, verbose_name="期号")
    
    title = models.CharField("标题",max_length=200)
    description = models.TextField("描述/导语/编者按", default = "", blank=True)
    author = models.CharField("作者", blank=True, max_length=200)
    content = MartorField() # 正文调用Markdown编辑框
    key = MartorField(blank=True) # 答案
    pub_date = models.DateTimeField("上传时间")
    attachment = models.ManyToManyField("Attach", verbose_name="附件", blank=True)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "文章"
        verbose_name_plural = verbose_name

class Attach(models.Model): # 附件 合并入Article？
    title = models.CharField("名称",max_length=200)
    file = models.ImageField("文件", upload_to="uploads/%Y/%m/%d/")
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "附件"
        verbose_name_plural = verbose_name

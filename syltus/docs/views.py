from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpRequest
from django.template import loader
from django.core.paginator import Paginator
from .models import *
"""
=============================================================
    docs/views.py
    SyltusDocs Nova: views

    (C)SyltusWorks 2024
=============================================================
"""
# Create your views here.
def index(r):
    list_latest = Article.objects.order_by("-pub_date")[:5]
    cat_list = Categoty.objects.order_by("id")
    issue_list = Issue.objects.order_by("year", "number")
    col_list = Column.objects.order_by("title")
    c = {
        "list_latest": list_latest,
        "cat_list": cat_list,
        "issue_list": issue_list,
        "col_list": col_list,
    }
    return render(r, "index.html", c)

def show(request, id):
    con = get_object_or_404(Article,pk=id)
    try:
        con_prev = Article.objects.get(pk = id - 1)
    except Article.DoesNotExist:
        con_prev = None
    
    try:
        con_next = Article.objects.get(pk = id + 1)
    except Article.DoesNotExist:
        con_next = None

    c = {
        "title": con.title,
        "description": con.description,
        "issue": con.issue,
        "author": con.author,
        "column": con.col,
        "pub_date": con.pub_date,
        "content": con.content,
        "extra": con.key,
        "attach": con.attachment.all(),
        "prev": con_prev,
        "next": con_next,
    }

    return render(request, "show.html", c)

def queue(request, page = 1):
    context = Article.objects.all()
    cat_list = Categoty.objects.order_by("id")
    issue_list = Issue.objects.order_by("year", "number")
    col_list = Column.objects.order_by("title")

    ArgNotEmpty = False

    args = request.GET
    if "issue" in args and args["issue"]!='':
        ArgNotEmpty = True
        context = context.filter(issue__id=args['issue'])
    if "cat" in args and args["cat"]!='':
        ArgNotEmpty = True
        context = context.filter(col__cat__id=args['cat'])
    if "col" in args and args["col"]!='':
        ArgNotEmpty = True
        context = context.filter(col__id=args['col'])
    if "title_contains" in args and args["title_contains"]!='':
        ArgNotEmpty = True
        context = context.filter(title__icontains=args['title_contains'])
    if "con_contains" in args and args["con_contains"]!='':
        ArgNotEmpty = True
        context = context.filter(content__icontains=args['con_contains'])

    pages = Paginator(context, 15)
    cpage = pages.page(page)


    c = {
        "con_count": context.count(),
        "page_range": pages.page_range,
        "total_pages": pages.num_pages,
        "pagenum": page,
        "current_page": cpage,
        "has_previous": cpage.has_previous(),
        "has_next": cpage.has_next(),
        "cat_list": cat_list, 
        "next_num": cpage.next_page_number() if cpage.has_next() else None,
        "prev_num": cpage.previous_page_number() if cpage.has_previous() else None,
        "issue_list": issue_list, 
        "col_list": col_list,
        "cat": int(args["cat"]) if "cat" in args and args["cat"]!='' else '',
        "col": int(args["col"]) if "col" in args and args["col"]!='' else '',
        "issue": int(args["issue"]) if "issue" in args and args["issue"]!='' else '',
        "title_contains": args["title_contains"] if "title_contains" in args else '',
        "con_contains": args["con_contains"] if "con_contains" in args else '',
        "not_empty": ArgNotEmpty,
        }

    return render(request, "queue.html", c)
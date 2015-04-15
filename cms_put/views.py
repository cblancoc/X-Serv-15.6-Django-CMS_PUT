from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.http import HttpResponseForbidden
from models import Table
from django.views.decorators.csrf import csrf_exempt


# Create your views here.


def all(request):
    list = Table.objects.all()
    out = ""
    if not list:
        out += "There are no blogs hosted on this page"
    else:
        out = "The blogs hosted on this page are: "
        for i in list:
            out += "<br><a href=blogs/" + i.blog + ">" + i.blog + "</a>\n"
    return HttpResponse(out)


@csrf_exempt
def urls(request, resource):
    if request.method == "GET":
        list = Table.objects.filter(blog=resource)
        if not list:
            return notfound(request, resource)
        out = " "
        for i in list:
            out += 'Blog \" ' + i.blog + ' \": '
            out += "<a href=http://" + i.url + ">" + i.url + "</a>\n"
        return HttpResponse(out)
    elif request.method == "PUT":
        new_blog = Table(blog=resource, url=request.body)
        new_blog.save()
        out = ("New blog added. ")
        return HttpResponse(out)
    else:
        return HttpResponseForbidden


def notfound(request, resource):
    out = ("Blog not found: " + resource)
    return HttpResponseNotFound(out)

import json

from django.db import models
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views import View

from book.models import BookInfo
from book.serializers import BookInfoSerializer


class BookInfoView(View):
    def get(self,request):
        books = BookInfo.objects.all()
        ser = BookInfoSerializer(books,many=True)
        # books_list = list()
        # for book in ser.data:
        #     books_list.append(book)
        # return JsonResponse(books_list,safe=False)
        return JsonResponse(ser.data, safe=False)

    def post(self,request):
        data = json.loads(request.body.decode())
        bs = BookInfoSerializer(data=data)
        bs.is_valid(True)
        bs.save()
        return JsonResponse(bs.data)


class BookInfoIDView(View):

    def get(self,request,id):
        book = BookInfo.objects.get(id=id)
        ser = BookInfoSerializer(instance=book)
        return JsonResponse(ser.data)


    def put(self,request,id):
        data = json.loads(request.body.decode())
        try:
            book = BookInfo.objects.get(id=id)
        except Exception as e:
            return HttpResponse({"message":e})

        ser = BookInfoSerializer(instance=book,data=data)
        ser.is_valid(raise_exception=True)
        ser.save()
        return JsonResponse(ser.data)

    def delete(self,request,id):
        book = BookInfo.objects.get(id=id)
        book.is_deleted = True
        book.save()
        return JsonResponse({"message":"删除成功"})


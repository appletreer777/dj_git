from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def hello(request):
    return HttpResponse('hello world')


# 在dev分支上书写代码
def dev_test(request):
    print('这是dev分支上的code')
    return HttpResponse('ok')
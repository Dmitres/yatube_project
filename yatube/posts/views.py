from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse ('Главненькая страничечка')

def group_posts(request, slug):
    return HttpResponse(f'О этот злаполучный {slug}')
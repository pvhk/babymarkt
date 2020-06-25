from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from ..models import Category, Ad

def list_ads(request,category_name):
    category = get_object_or_404(Category, name=category_name)
    ads = Ad.objects.filter(category=category)
    return HttpResponse(ads)
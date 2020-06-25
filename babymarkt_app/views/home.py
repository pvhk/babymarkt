from django.shortcuts import render
from django.db.models import Count
from ..models import Category
from ..typesearch.typesense_utils import TypeSearch

def index(request):
    most_popular_categories = Category.objects.annotate(number_of_ads=Count('ad')).order_by('-number_of_ads')[:5]
    context = {
        'most_popular_categories':most_popular_categories
        }
    return render(request, 'babymarkt_app/index.html', context)
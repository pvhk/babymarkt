from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from ..models import Ad, Picture
from django.contrib.auth.decorators import login_required
from ..forms.BabyMarktForms import NewAdForm
from ..typesearch.typesense_utils import TypeSearch
def index(request):
    ads = Ad.objects.all()
    return HttpResponse(ads)

@login_required
def new(request):
    if request.method == "POST":
        form = NewAdForm(request.POST, request.FILES)
        if form.is_valid():
            ad = Ad(category=form.cleaned_data["category"], title=form.cleaned_data["title"], text=form.cleaned_data["text"], price=form.cleaned_data["price"], user=request.user)
            ad.save()
            files = request.FILES.getlist('file_field')
            for f in files:
                new_pic = Picture(ad=ad,url=f)
                new_pic.save()
            TypeSearch.index_ad(ad.id, form.cleaned_data["title"], form.cleaned_data["text"], int(form.cleaned_data["price"]), True, str(form.cleaned_data["category"]), str(files[0]), '2020-03-21 21:35:43.985473')
            return HttpResponseRedirect("/")
    else:
        form = NewAdForm()
    return render(request, 'babymarkt_app/ads/postAd.html',{'form':form})

def detail(request, ad_id):
    current_ad = get_object_or_404(Ad,pk=ad_id)
    pictures = Picture.objects.filter(ad=current_ad)
    current_ad.pictures = pictures
    return render(request, 'babymarkt_app/ads/singleAd.html', {'ad':current_ad})

def search(request):
    search_str = request.GET.get('query')
    ads = TypeSearch.search(search_str)
    return render(request, 'babymarkt_app/ads/searchAds.html', {"ads":ads})

@login_required
def edit(request, ad_id):
    ad = get_object_or_404(Ad, pk=ad_id)
    if ad.user != request.user:
        return HttpResponseRedirect('/')
    form = NewAdForm(initial={'title':ad.title, 'text':ad.text, 'price':ad.price, 'category':ad.category})
    return render(request, 'babymarkt_app/ads/edit_ad.html', {'form':form})

@login_required
def delete(request, ad_id):
    ad = get_object_or_404(Ad, pk=ad_id)
    if ad.user != request.user:
        return HttpResponseRedirect('/')
    ad.delete()
    return HttpResponseRedirect('/')
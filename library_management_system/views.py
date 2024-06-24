from django.shortcuts import render
from Train.models import Train,Station

def home(request,category_slug= None): # initially dhore nicchi je category_slug None thakbe karon hocche user first time home page e asle se normal page dekhbe, se filter korte chaile category te click korlei sei category er slug ta capture korbo ar seta tokhn ar None thakbe na
    
    data =  Train.objects.all() # sob post gula ke niye aslam
    if category_slug is not None: # ekhn category slug jodi None na hoy tar mane sekhane value ache
        category = Station.objects.get(slug=category_slug) # slug je field model e likhechilam seta = amader Station slug kore dilam taile ekhn kon category er slug sei category object peye jabo
        data =  Train.objects.filter(station=category) # post er category te category object bosiye filter korlam, ager data er sathe overright hoye jabe
    categories = Station.objects.all() # sob category dekhabo
    
    return render(request, 'home.html', {'data' : data, 'category' : categories})
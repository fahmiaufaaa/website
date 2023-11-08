from django.shortcuts import render

# Create your views here.
def trending(request):
    return render(request, 'menu/trending.html')

def sport(request):
    return render(request, 'menu/sport.html')

def politics(request):
    return render(request, 'menu/politics.html')

def lifestyle(request):
    return render(request, 'menu/lifestyle.html')

def entertainment(request):
    return render(request, 'menu/entertainment.html')

def healty(request):
    return render(request, 'menu/healty.html')
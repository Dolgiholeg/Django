from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponsePermanentRedirect

# Create your views here.
def index(request):
    #return HttpResponse('<h1>Hello world</h1>')
    return HttpResponsePermanentRedirect('home/')

def about(request):
    return HttpResponse('<b>О нашей фирме</b>')

def home(request):
    return render(request, 'index.html')

def contacts(request):
    return render(request,'contacts.html')

def workers(request):
    return render(request,'workers.html')

def month(req,id):
    id=int(id)
    month=['март','апрель','май']
    workers = ['Меркурий', 'Кобальт', 'Вольфрам']
    imgs = ['img/Merkury.png', 'img/Rabotnik_mesyca.jpg', 'img/Кот-работник.jpg']
    data={'k1':month[id],'k2':workers[id],'k3':imgs[id]}
    return render(req,'month.html',context=data)

def produkt(req,id):
    id=int(id)
    month=['продукт1','продукт2','продукт3']
    workers = ['Яблоко', 'Груша', 'Ананас']
    imgs = ['img/Яблоко.jpg', 'img/Груша.jpg', 'img/Ананас.jpg']
    data={'k4':month[id],'k5':workers[id],'k6':imgs[id]}
    return render(req,'produkt.html',context=data)

def spisok(req):
    firmsall=['apple','ibm','microsoft','oracle','amigo','samsung']
    data={'firms':firmsall}
    return render(req,'spisok.html',context=data)
def proverka(req,year):
    data={'year': year}
    return render(req,'proverka.html',context=data)
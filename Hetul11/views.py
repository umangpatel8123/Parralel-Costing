from bs4 import BeautifulSoup
from django.contrib.sites import requests
from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from django.shortcuts import render
import sys
from subprocess import run,PIPE
from bs4 import BeautifulSoup
import requests
import html5lib
import smtplib

# global fp
# global am





def index(request):
    # return HttpResponse("index.html")
    return render(request, "index.html")


def iphone13(request):
    global fp
    global am
    global Filpkart
    global filpkart
    # product_name = request.GET['value']
    # product_name = request.GET["name"]
    products = Product.objects.all()
    for product in products:
        if product.product_name=="iphone13":
            fp=product.filpkart_id
            am=product.amazon_id
    print(fp)
    print(am)
    price=trackprices(fp,am)
    # if Filpkart and filpkart in price:
    #     link=fp
    # else:
    #     link=am

    # products = Product.objects.filter(Product_name=product_name)
    # products = Product.objects()
    # print(Product[0].filpkart_id)
    # print(Product[0].amazon_id)
    params = {'product': products}
    print(params)
    return render(request, 'iphone13.html',{'data1':price})


def search(request):
    # product_name = request.GET['name']
    # # product_name = request.GET["name"]
    #
    # products = Product.objects.filter(product_name=product_name)
    # # products = Product.objects()
    # print(products)
    # params = {'product': products}
    # print(params)
    return render(request, "search.html")

def nothing(request):
    global fp
    global am
    global Filpkart
    global filpkart
    products = Product.objects.all()
    for product in products:
        if product.product_name == "nothing":
            fp = product.filpkart_id
            am = product.amazon_id
    print(fp)
    print(am)
    price = trackprices(fp, am)
    params = {'product': products}
    print(params)
    return render(request, "nothing.html",{'data1': price})


def zflip(request):
    global fp
    global am
    global Filpkart
    global filpkart
    # product_name = request.GET['value']
    # product_name = request.GET["name"]
    products = Product.objects.all()
    for product in products:
        if product.product_name == "zflip":
            fp = product.filpkart_id
            am = product.amazon_id
    print(fp)
    print(am)
    price = trackprices(fp, am)
    params = {'product': products}
    print(params)
    return render(request, "zflip.html",{'data1': price})


def motoe40(request):
    global fp
    global am
    global Filpkart
    global filpkart
    products = Product.objects.all()
    for product in products:
        if product.product_name == "motoe40":
            fp = product.filpkart_id
            am = product.amazon_id
    print(fp)
    print(am)
    price = trackprices(fp, am)
    params = {'product': products}
    print(params)
    return render(request, "motoe40.html",{'data1': price})


def airpods(request):
    global fp
    global am
    global Filpkart
    global filpkart
    # product_name = request.GET['value']
    # product_name = request.GET["name"]
    products = Product.objects.all()
    for product in products:
        if product.product_name == "airpods":
            fp = product.filpkart_id
            am = product.amazon_id
    print(fp)
    print(am)
    price = trackprices(fp, am)
    params = {'product': products}
    print(params)
    return render(request, "airpods.html", {'data1': price})


def mivi(request):
    global fp
    global am
    global Filpkart
    global filpkart
    # product_name = request.GET['value']
    # product_name = request.GET["name"]
    products = Product.objects.all()
    for product in products:
        if product.product_name == "mivi":
            fp = product.filpkart_id
            am = product.amazon_id
    print(fp)
    print(am)
    price = trackprices(fp, am)
    params = {'product': products}
    print(params)
    return render(request, "mivi.html", {'data1': price})


def noice(request):
    global fp
    global am
    global Filpkart
    global filpkart
    # product_name = request.GET['value']
    # product_name = request.GET["name"]
    products = Product.objects.all()
    for product in products:
        if product.product_name == "noice":
            fp = product.filpkart_id
            am = product.amazon_id
    print(fp)
    print(am)
    price = trackprices(fp, am)
    params = {'product': products}
    print(params)
    return render(request, "noice.html",{'data1': price})


def boat131(request):
    global fp
    global am
    global Filpkart
    global filpkart
    # product_name = request.GET['value']
    # product_name = request.GET["name"]
    products = Product.objects.all()
    for product in products:
        if product.product_name=="boat131":
            fp=product.filpkart_id
            am=product.amazon_id
    print(fp)
    print(am)
    price=trackprices(fp,am)
    params = {'product': products}
    print(params)
    return render(request, "boat131.html", {'data1': price})

def trackprices(fp,am):
    global flipkartproduct
    global Amazonproduct
    flipkartproduct = fp
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'}
    if flipkartproduct:
        flipkartResponse = requests.get(fp, headers=headers)
        AmazonResponse = requests.get(am, headers=headers)
        flipkartsoup = BeautifulSoup(flipkartResponse.content, 'html5lib')
        Amazonsoup = BeautifulSoup(AmazonResponse.content, 'html5lib')
        flipkartproducteprice = float(flipkartsoup.find('div', attrs='_30jeq3 _16Jk6d').text.replace(',', '')[1:])
        amazonproducteprice = float(Amazonsoup.find('span', attrs='a-offscreen').text.replace(',', '')[1:])
        print("flipkart prics is  :  " + str(flipkartproducteprice))
        output = "Filpkart price : " + str(flipkartproducteprice)
        output2 = "Amazon price : " + str(amazonproducteprice)
        output3 = "Filpkart or Azmazon : " +str(flipkartproducteprice)
        # print("Amazon prics is  :  "+str(amazonproducteprice))
        if flipkartproducteprice > amazonproducteprice:
            print("Amazon price is less then flipkart and price is : " + str(amazonproducteprice))
            return output2
        elif flipkartproducteprice == amazonproducteprice:
            return output3
        else:
            print(" price is less then amazon and price is : " + str(flipkartproducteprice))
            return output

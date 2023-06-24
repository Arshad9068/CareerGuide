from django.shortcuts import render , redirect
from django.contrib.auth import authenticate
from django.http import HttpResponse
from .models import Register
import requests

# Create your views here.

def login(request):
    if request.method == "POST":
        uname = request.POST.get('uname')
        pwd = request.POST.get('pass')
        user = authenticate(request, username=uname, password=pwd)
        if user is not None:
            return render(request,'login.html')
        
        else:
            return HttpResponse("Succesfully logged in")
            
    return render(request, 'login.html')


def signup(request):
    if request.method == "POST":
        emails = request.POST.get('email')
        uname = request.POST.get('uname')
        pwd = request.POST.get('pass')
        edu = request.POST.get('education')
        country = request.POST.get('country')
        c_code = request.POST.get('country_code')
        mobile = request.POST.get('mobile')
        if Register.objects.filter(username=uname).count() > 0:
            
            error = "Username already exists"
            return render(request, 'signup.html', {'error': error})
        else:
            user = Register(username=uname, emailid=emails, password=pwd, education=edu, country=country, countryCode=c_code, mobile=mobile)
            user.save()
            return redirect('/login')
    country=[]
    country_c={}
    response= requests.get('https://restcountries.com/v3.1/all').json()
    for i in response:
        country.append(i['name']['common'])
        # print(i['name']['common'])
    country.sort()

    for i in response:
        if len(i['idd'])==0:
            name="country"
            precode="code"
            country_c.update({name:code})
        else:
            name=i['name']['common']
            precode=i['idd']['suffixes']
            code=i['idd']['root']+precode[0]
            country_c.update({name:code})
        sortkeys= list(country_c.keys())
        sortkeys.sort()
        country_code={i:country_c[i] for i in sortkeys}
    return render(request, 'signup.html',{'country': country,'country_code':country_code})

# "idd":{"root":"+9","suffixes":["1"]
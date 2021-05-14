from django.forms.widgets import PasswordInput
from django.http.response import HttpResponseRedirect
from nse.forms import StudentRegistration,NiftyDataForm,BankNiftyDataForm
from .models import banknifty,nifty,Customer,members
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.models import User,auth
from django.shortcuts import redirect,render
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from datetime import datetime, timedelta



import random
import string

# Approach first
# get random password pf length 8 with letters, digits, and symbols

# Output $z#m;-fb


#Home view - Project Description
@csrf_protect
@login_required(login_url='login')
def home(request):
    niftydata = nifty.objects.all()
    bankniftydata = banknifty.objects.all()
    context = {'niftydata':niftydata,'bankniftydata':bankniftydata}
    return render(request, 'home.html',context)

def welcome(request):
    return render(request, 'testing.html')


# Add new customers
def add_show(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            ms = fm.cleaned_data['membership']

            # Password Generation
            password_characters = string.ascii_letters + string.digits + string.punctuation
            password = ''.join(random.choice(password_characters) for i in range(8))
            print("Random password is:", password)

            # Subcription end date calculation

            if ms == "Trial":
                sub_end_date = datetime.now() + timedelta(days=3)
            else:
                sub_end_date = datetime.now() + timedelta(days=30)


            reg = members(name=nm,email=em,password=password,membership=ms,subscriptionenddate=sub_end_date,status="Active")
            reg.save()
            fm = StudentRegistration()

    else:
        fm = StudentRegistration()
    stud = members.objects.all()

    return render(request, 'addandshow.html',{'form':fm,'stu':stud})


# Add new customers
def addnsedata(request):
    if request.method == 'POST':
        print(request.POST)
        if 'btnform1' in request.POST:
            print("True")

            nf = NiftyDataForm(request.POST)
            
            # Nifty Form
            if nf.is_valid():
                si = nf.cleaned_data['signal']
                en = nf.cleaned_data['entry']
                ta = nf.cleaned_data['target']
                ad = nf.cleaned_data['advisory']


                if (si != "") and (en != "") and (ta != "") and (ad != ""):
                    niftyData = nifty(signal=si,entry=en,target=ta,advisory=ad)
                    niftyData.save()
                    

        if 'btnform2' in request.POST:

            bnf = BankNiftyDataForm(request.POST)



            #BankNifty Form
            if bnf.is_valid():
                bsignal = bnf.cleaned_data['signal']
                bentry = bnf.cleaned_data['entry']
                btarget = bnf.cleaned_data['target']
                badvisory = bnf.cleaned_data['advisory']

                print(bsignal)
                print(bentry)
                print(btarget)
                print(badvisory)


                if (bsignal != "") and (bentry != "") and (btarget != "") and (badvisory != ""):
                    print("Not Empty")
                    BankniftyData = banknifty(signal=bsignal,entry=bentry,target=btarget,advisory=badvisory)
                    BankniftyData.save()
                    

    else:
        nf = NiftyDataForm()
        bnf = BankNiftyDataForm()
    nf = NiftyDataForm()
    bnf = BankNiftyDataForm()
    niftyAllData = nifty.objects.all()
    BankniftyAllData = banknifty.objects.all()


    return render(request, 'addrecord.html',{'niftyform':nf,'bankniftyform':bnf,'niftydata':niftyAllData,'bankniftydata':BankniftyAllData})

def OptionChain(request):

    import requests
    import json
    import pandas as pd 

    url_oc = "https://www.nseindia.com/option-chain"
    url = f"https://www.nseindia.com/api/option-chain-indices?symbol=NIFTY"
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, '
                            'like Gecko) '
                            'Chrome/80.0.3987.149 Safari/537.36',
            'accept-language': 'en,gu;q=0.9,hi;q=0.8', 'accept-encoding': 'gzip, deflate, br'}
    # session = requests.Session()
    # request = session.get(url_oc, headers=headers, timeout=5)
    # cookies = dict(request.cookies)
    # response = session.get(url, headers=headers, timeout=5, cookies=cookies)
    response = requests.get(url, headers=headers, timeout=5)

    newDict =  response.json()
    listOfDict = newDict['records']['data']
    print(type(listOfDict))

    return render(request, 'OptionChain.html',{'listOfDict':listOfDict})


# Edit ExistingCustomer
def edit_data(request,id):
    if request.method == "POST":
        pi =  members.objects.get(pk=id)
        password_characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(password_characters) for i in range(8))
        print("Random password is:", password)
        pi.password = password
        fm= StudentRegistration(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect('/add')
    else:
        pi =  members.objects.get(pk=id)
        fm = StudentRegistration(instance=pi)
    return render(request, 'updateuser.html',{'form':fm})


def registeredusers(request):
    userlt = Customer.objects.all()
    print(userlt)
    return render(request, 'registeredusers.html',{'userlt':userlt,"charts_form": "btn-disabled"})
 

# Delete ExistingCustomer
def delete_data(request,id):
    if request.method == 'POST':
        pi = members.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/add')


#Login View - Login page
@csrf_protect
def login(request):
    
    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']
        print(username)
        if User.objects.filter(username=username).exists():
            user=auth.authenticate(username=username,password=password)
            print(user)
            if user is not None:
                auth.login(request,user)
                # messages.info(request, f"You are now logged in as {username}")
                return redirect('home')
            else:
                messages.info(request,'incorrect password')
                return redirect('login')
        else:
            messages.error(request,"user doesn't exists")
            return redirect('login')

    else:
        
        return render(request,template_name = "login.html")


#Register View - User Registration
@csrf_protect
def register(request):

    if request.method == 'POST':

        username= request.POST['username']
        fathername= request.POST['fathername']
        mobile= request.POST['phone_number']
        email= request.POST['email']
        address= request.POST['address']


        if Customer.objects.filter(email=email).exists():
            messages.info(request,"Email already exists")
            return redirect('register')
        else:
            user=Customer.objects.create(name=username,fathername=fathername,mobile=mobile,email=email,address=address)    
            user.save()
            print("User Created")
            messages.info(request,"Thank you for filling out your information! We will be in touch with you shortly")
            return redirect('login')

        return redirect('login')
    else:

        return render(request, 'register.html')

#Logout View - User Logout
def logout(request):

    auth.logout(request)
    request.session.flush()
    print("logged out")
    messages.success(request,"Successfully logged out")
    for sesskey in request.session.keys():
        del request.session[sesskey]

    return redirect('login')     


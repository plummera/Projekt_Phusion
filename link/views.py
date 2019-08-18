"""
Definition of views.
"""

from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpRequest, HttpResponse
from django.template import RequestContext
from .forms import TwitterNameForm
from link.forms import BootstrapAuthenticationForm, SignUpForm, User1Form, User2Form
from .models import Analysis, Psychic, Update, Tweet, Intel, Cryptocurrency
from .watson import insight, compare, getUser, getFBfriends, getFBcomments, getFBprofilePic, getFBposts, getTwitterPosts, getFBprofile, end_result
from .cryptocurrency import getBalance
from django.contrib.auth import login, logout, authenticate

import decimal
import datetime
import os
import telnetlib
import requests
import json

def about(request):
    """
    Renders the about page.
    """
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title': 'What is this?',
            'message': "This is a proof of concept maneuver to leverage C&C allocation capabilities to aggregate distributed conncectivity, unilaterally binding remote pools of unique nodes and identifiers.",
        },
    )

def blockchain(request):
    """
    Renders the contact page.
    """
    assert isinstance(request, HttpRequest)

    r = requests.get('https://www.cryptocompare.com/api/data/coinlist/')
    print("RAWR!!!... : " + str(r.text))
    currencies = json.loads(str(r.text))

    count = 0
    for chains in currencies['Data']:
        print("Check Check.... echo: " + str(chains))
        FullyPremined = currencies['Data'][chains]['FullyPremined']
        print("")
        print("How we roll... " + str(FullyPremined))
        print("")

        count += 1

    return render(request, 'app/blockchain.html', {
        'message': currencies['Message'],
        'embed': currencies['Data'].items,
        'currencies': currencies['Data'],
        'totalBlockchains': count,
    })

def contact(request):
    """
    Renders the contact page.
    """
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
    )

def home(request):
    """
    Renders the home page.
    """
    assert isinstance(request, HttpRequest)

    # Update Object
    updates = Update.objects.all

    return render(
        request,
        'app/index.html',
        {
            'updates': updates,
        }
    )

def link(request):
    """
    Renders Link's AutoBot
    """
    assert isinstance(request, HttpRequest)
    link = get_object_or_404(Psychic, pk=1)

    return render(
        request,
        'app/link.html',
        {
            'link': link,
            'title': 'Turtle Shell v2.2',
            'message': 'If you do not know what is happening here, rememeber you can ask.',
            'host': link.host,
            'port': link.port,
            'telnet': telnet,
        },
    )

def login_form(request):
    if request.method == 'POST':
        form = BootstrapAuthenticationForm(data=request.POST)
        if form.is_valid():
            print("FORM IS VALID!")
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            error_messages = "Let's Ride"
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
        else:
            print("FORM IS -=INVALID=-")
            error_messages = "You did not fill out the form properly"
    else:
        form = BootstrapAuthenticationForm()

    return render(request, 'app/login.html', {'form': form})

def logout_form(request):
    """
    Renders the logout function for all logout requests.
    """
    if request.method == 'GET':
        print("LOGGING OUT!")
        logout(request)
    else:
        print("ALREADY LOGGED OUT!")
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
    )

def signup_form(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, first_name=first_name, last_name=last_name, email=email, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()

    title = 'You need to login'
    year = datetime.date.year

    return render(request, 'app/signup.html', {'form': form, 'title': title, 'year': year})

def staging(request):
    """
    The Staging Staging Area
    """
    assert isinstance(request, HttpRequest)

    form = BootstrapAuthenticationForm()

    if request.method == 'POST':
        form1 = User1Form(request.POST)
        if form.is_valid():
            form.save()
            user1 = form.cleaned_data.get('user1')
            return redirect('home')
        form2 = User2Form(request.POST)
        if form.is_valid():
            form.save()
            user2 = form.cleaned_data.get('user2')
            return redirect('home')
    else:
        form1 = User1Form()
        form2 = User2Form()

    login_form(request)

    stats = end_result()

    analysis            = stats[0]
    data1               = stats[1]
    data2               = stats[2]
    FBProfilePic1       = stats[3]
    FBProfilePic2       = stats[4]
    post1               = stats[5]
    post2               = stats[6]
    profile             = stats[7]
    similarityLow       = stats[8]
    similarityMedium    = stats[9]
    similarityVeryHigh  = stats[10]
    tweets1             = stats[11]
    tweets2             = stats[12]
    user1               = stats[13]
    user2               = stats[14]
    user1_list          = stats[15]
    user2_list          = stats[16]

    return render(
        request,
        'app/staging_area.html',
        {
            'analysis': analysis,
            'data1': data1,
            'data2': data2,
            'FBProfilePic1': FBProfilePic1,
            'FBProfilePic2': FBProfilePic2,
            # 'FBCoverPic1': FBCoverPic1,
            # 'FBCoverPic2': FBCoverPic2,
            'form': BootstrapAuthenticationForm,
            'post1': post1,
            'post2': post2,
            'profile': profile,
            'similarityLow': similarityLow,
            'similarityMedium': similarityMedium,
            'similarityVeryHigh': similarityVeryHigh,
            'tweets1': tweets1,
            'tweets2': tweets2,
            'user1': user1,
            'user2': user2,
            'user1_list': user1_list,
            'user2_list': user2_list,
        },
    )

def telnet():

    link = get_object_or_404(Psychic, pk=1)

    host = 'theland.notroot.com'
    port = 5000

    s = telnetlib.Telnet(host, port)
    s.set_debuglevel(9)

    if s:
        print ('Connected!')
    else:
        print ('Unable to connect')
        os.sys.exit()

    link.data = s.read_until("By what name do you wish to be known?".encode("ascii"))
    return link.data
    s.write(link.name + '\n')
    s.close()

def tos(request):
    """
    Renders the contact page.
    """
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/tos.html',
    )

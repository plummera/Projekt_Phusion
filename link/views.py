"""
Definition of views.
"""

from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpRequest, HttpResponse
from django.template import RequestContext
from .forms import TwitterNameForm
from link.forms import BootstrapAuthenticationForm, SignUpForm
from .models import Psychic, Update, Tweet, Intel, Cryptocurrency
from .watson import insight, compare, getUser, getFBfriends, getFBcomments, getFBCoverPic, getFBprofilePic, getFBposts, getTwitterPosts, getFBprofile
from .cryptocurrency import getBalance
from django.contrib.auth import login, authenticate

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

    title = "You need to login"
    year = datetime.date.year

    return render(request, 'app/signup.html', {'form': form, 'title': title, 'year': year})

def staging(request):
    """
    The Staging Staging Area
    """
    assert isinstance(request, HttpRequest)

    login_form(request)

    origin_FB = 'me'
    destination_FB = 'me'
    origin_twitter = 'AnthonyTPlummer'
    destination_twitter = 'AnthonyTPlummer'

    # Getting User Information from Twitter Profile
    user1 = getUser(origin_twitter)
    user2 = getUser(destination_twitter)

    # Getting Posts from FaceBook
    post1 = getFBposts(origin_FB)
    post2 = getFBposts(destination_FB)

    # Gettings Origin Profile from Facebook
    profile = getFBprofile(origin_FB)

    # Getting the most Recent 200 Tweets from Twitter
    tweets1 = getTwitterPosts(origin_twitter)
    tweets2 = getTwitterPosts(destination_twitter)

    #The IBM Watson Public Feed Analysis Results
    data1 = insight(tweets1)
    data2 = insight(tweets2)

    # Creating Object for project deliverable
    package1 = get_object_or_404(Intel)
    package2 = get_object_or_404(Intel)

    # Creating a place store the metrics returned and a column to classify them
    # (for Profile #1)
    package1.metric = []
    package1.category = []

    # Creating a place store the metrics returned and a column to classify them
    # (for Profile #2)
    package2.metric = []
    package2.category = []

    user1_list = []
    user2_list = []

    user1_list = [None]*(len(package1.metric)+len(package1.category))
    user1_list[::2] = package1.metric
    user1_list[1::2] = package1.category


    user2_list = [None]*(len(package2.metric)+len(package2.category))
    user2_list[::2] = package2.metric
    user2_list[1::2] = package2.category

    user1_list = zip(package1.metric, package1.category)
    user2_list = zip(package2.metric, package2.category)

    #Loop to populate categories returned from Watson
    for a in data1[0]:
        package1.category.append(a)
    for a in data2[0]:
        package2.category.append(a)

    #Loop to populate metric percentages returned from Watson
    for i in data1[1]:
        package1.metric.append(i)
    for i in data2[1]:
        package2.metric.append(i)

    result = compare(data1[2], data2[2])

    # Getting FaceBook Profile Pic
    FBProfilePic1 = getFBprofilePic(origin_FB)
    FBProfilePic2 = getFBprofilePic(destination_FB)

    # Getting Cover Picture from Facebook
    FBCoverPic1 = getFBCoverPic(origin_FB)
    FBCoverPic2 = getFBCoverPic(destination_FB)

    if profile:

        return render(
            request,
            'app/staging_area.html',
            {
                'post1': post1,
                'post2': post2,
                'profile': profile,
                'result': result,
                'user1': user1,
                'user2': user2,
                'tweets1': tweets1,
                'tweets2': tweets2,
                'user1_list': user1_list,
                'user2_list': user2_list,
                'FBProfilePic1': FBProfilePic1,
                'FBProfilePic2': FBProfilePic2,
                'FBCoverPic1': FBCoverPic1,
                'FBCoverPic2': FBCoverPic2,
                'form': BootstrapAuthenticationForm,
            },
        )

    else:
        return render(request, 'app/login')

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

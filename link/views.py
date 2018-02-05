"""
Definition of views.
"""

from django.shortcuts import get_object_or_404, render
from django.http import HttpRequest
from django.template import RequestContext
from .forms import TwitterNameForm
from .models import Psychic, Update, Tweet, Intel, Profile
from .watson import insight, compare, getUser, getFBfriends, getFBcomments, getFBCoverPic, getFBprofilePic, getFBposts, getTwitterPosts
from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder


import datetime
import os
import telnetlib

def home(request):
    """
    Renders the home page.
    """
    assert isinstance(request, HttpRequest)

    origin_FB = 'me'
    destination_FB = 'monerocurrency'
    origin_twitter = 'AnthonyTPlummer'
    destination_twitter = 'MoneroAlert'

    # Update Object
    updates = Update.objects.all

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

    result = compare(data1[2], data2[2])

    # Getting Posts from FaceBook
    post1 = getFBposts(origin_FB)
    post2 = getFBposts(destination_FB)

    # Getting FaceBook Profile Pic
    FBProfilePic1 = getFBprofilePic(origin_FB)
    FBProfilePic2 = getFBprofilePic(destination_FB)

    # Getting Cover Picture from Facebook
    FBCoverPic1 = getFBCoverPic(origin_FB)
    FBCoverPic2 = getFBCoverPic(destination_FB)

    # Getting User Information from Twitter Profile
    user1 = getUser(origin_twitter)
    user2 = getUser(destination_twitter)

    return render(
        request,
        'app/index.html',
        {
            'FBProfilePic1': FBProfilePic1,
            'FBProfilePic2': FBProfilePic2,
            'FBCoverPic1': FBCoverPic1,
            'FBCoverPic2': FBCoverPic2,
            'package1': package1,
            'package2': package2,
            'post1': post1,
            'post2': post2,
            'result': result,
            'tweets1': tweets1,
            'tweets2': tweets2,
            'updates': updates,
            'user1': user1,
            'user2': user2,
            'user1_list': user1_list,
            'user2_list': user2_list,
        }
    )

def contact(request):
    """
    Renders the contact page.
    """
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
    )

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
            'message': "This is a switching and control center for a guild of players operating in a virtual gaming environment.",
        },
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
            'title': "Link's Humble Abode",
            'message': 'If you do not know what is happening here, rememeber you can ask.',
            'host': link.host,
            'port': link.port,
            'telnet': telnet,
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

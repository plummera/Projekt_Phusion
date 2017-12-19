"""
Definition of views.
"""

from django.shortcuts import get_object_or_404, render
from django.http import HttpRequest
from django.template import RequestContext
from .forms import TwitterNameForm
from .models import Psychic, Update, Tweet, Intel
from .watson import analyze, insight, compare, getUser
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

    tweets1 = analyze("AnthonyTPlummer")
    tweets2 = analyze("BankOfAmerica")

    updates = Update.objects.all
    data1 = insight(tweets1)
    data2 = insight(tweets2)
    user1 = getUser("AnthonyTPlummer")
    user2 = getUser("BankOfAmerica")
    user1_list = []
    user2_list = []

    print ("NOW FOR THE GOOD PART:")
    print ("")
    print "User #1: " + user1.name
    print ("")
    print "User #2: " + user2.name
    print ("")
    print ("So it works: Great!! To NYC")
    print ("Name: " + user1.name)
    print ("Location: " + user1.location)
    print ("")
    print ("Other Name: " + user2.name)
    print ("Location: " + user2.location)
    print ("")

    package1 = get_object_or_404(Intel)
    package2 = get_object_or_404(Intel)

    package1.metric = []
    package1.category = []

    package2.metric = []
    package2.category = []

    for i in data1[1]:
        package1.metric.append(i)

    for a in data1[0]:
        package1.category.append(a)

    for i in data2[1]:
        package2.metric.append(i)

    for a in data2[0]:
        package2.category.append(a)

    list1 = package1.metric
    list2 = package1.category
    user1_list = [None]*(len(list1)+len(list2))
    user1_list[::2] = list1
    user1_list[1::2] = list2

    list3 = package2.metric
    list4 = package2.category
    user2_list = [None]*(len(list3)+len(list4))
    user2_list[::2] = list3
    user2_list[1::2] = list4

    user1_list = zip(list1, list2)
    user2_list = zip(list3, list4)

    result = compare(data1[2], data2[2])

    return render(
        request,
        'app/index.html',
        {
            'updates': updates,
            'tweets1': tweets1,
            'tweets2': tweets2,
            'package1': package1,
            'package2': package2,
            'result': result,
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
        print 'Connected!'
    else:
        print 'Unable to connect'
        os.sys.exit()

    link.data = s.read_until("By what name do you wish to be known?")
    return link.data
    s.write(link.name + '\n')
    s.close()

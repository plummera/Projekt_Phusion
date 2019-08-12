import sys
import requests
import json
import operator
import twitter
import facebook
import requests
import decimal
import datetime
import os
import telnetlib

from datetime import datetime
from django.http import JsonResponse
from ibm_watson import PersonalityInsightsV3
from django.utils.encoding import force_text
from django.core.serializers.json import DjangoJSONEncoder
from django.core import serializers
from django.shortcuts import get_object_or_404, render, redirect
from .credentials import *
from .models import Analysis, Psychic, Update, Tweet, Intel, Cryptocurrency

#FB credentials
r = requests.get("https://graph.facebook.com/oauth/access_token?grant_type=client_credentials&client_id=" + facebook_client_ID + "&client_secret=" + facebook_client_secret + "")
access_token = r.text.split('=')[0]

graph = facebook.GraphAPI(access_token=graph_key, version='2.10')

class LazyEncoder(DjangoJSONEncoder):
    def default(self, obj):
        if isinstance(obj, text):
            return force_text(obj)
        return super(LazyEncoder, self).default(obj)


# Getting the most recent 200 Posts from Twitter
def getTwitterPosts(handle):
    twitter_api = twitter.Api(consumer_key=twitter_consumer_key, consumer_secret=twitter_consumer_secret, access_token_key=twitter_access_token, access_token_secret=twitter_access_secret)
    statuses = twitter_api.GetUserTimeline(screen_name=handle, count=700, include_rts=False)

    return statuses

# FACEBOOK IS LAME!!!!!! FOR This
#
# def getFBCoverPic(handle):
#     pic = graph.request('/' + handle + '?fields=cover')
#
#     return pic['cover']

def getFBprofilePic(handle):
    cover = graph.request('/' + handle + '?fields=picture')

    return cover['picture']['data']

def getFBprofile(handle):
    profile = graph.request('/' + handle + '?fields=id,name,email')

    return profile

def getFBPostPicture(handle):
    picture = graph.request('/' + handle + '?fields=posts{picture}')

    return picture['posts']['data']

def getFBposts(handle):
    posts = graph.request('/' + handle + '?fields=posts.limit(75){message,picture,story,link,full_picture,created_time,description,permalink_url}')

    for post in posts['posts']['data']:
        post['created_time'] = datetime.strptime(post['created_time'], "%d-%M-%Y")


    return posts['posts']['data']

def getFBfriends(handle):
    friends = graph.get_connections(id=handle, connection_name='friends')

    return friends

def getFBcomments(handle):
    comments = graph.get_connections(id=handle, connection_name='comments')

    return comments

def getUser(handle):
    twitter_api = twitter.Api(consumer_key=twitter_consumer_key, consumer_secret=twitter_consumer_secret, access_token_key=twitter_access_token, access_token_secret=twitter_access_secret)
    user = twitter_api.GetUser(screen_name=handle)

    return user

def insight(statuses):

    text = ""

    for status in statuses:
        text += status.text

    personality_insights = PersonalityInsightsV3(version="2016-10-19",username=pi_username,password=pi_password)

    # personality_insights.set_detailed_response(False)

    pi_result = personality_insights.profile(
        text,
        accept='application/json',
        content_type='text/plain',
        consumption_preferences=False,
        raw_scores=False
    )

    data = flatten(pi_result)

    category = []
    result = []

    for keys in data['id']:
        category.append(keys)

    for keys in data['percentile']:
        result.append(keys)

    return result, category, data

#This function is used to flatten the result
#from the Watson PI API
def flatten(orig):
    data = {}
    data['id'] = []
    data['percentile'] = []

    orig = orig.get_result()

    for personality in orig['personality']:
        print("")
        # print("Trait ID = " + str(personality['trait_id']))
        print("Name = " + str(personality['name']))
        data['id'].append(personality['name'])
        # print("Category = " + str(personality['category']))
        print("Percentile = " + str(personality['percentile']))
        data['percentile'].append(personality['percentile'])
        for children in personality['children']:
            print("")
            # print("Trait ID = " + str(children['trait_id']))
            print("Name = " + str(children['name']))
            data['id'].append(children['name'])
            # print("Category = " + str(children['category']))
            print("Percentile = " + str(children['percentile']))
            data['percentile'].append(children['percentile'])

    print("")
    print("Yahtzee!")
    print("")
    return data


#This function is used to compare the results from
#the Watson PI API
def compare(dict1, dict2):
    compared_data = zip(dict1, dict2)
    compared_results = []
    for x,y in compared_data:
        compared_results.append(abs(x - y))

    return compared_results

#The two Twitter handles
user_handle = "AnthonyTPlummer"

#Analyze the user's tweets using the Watson PI API
# user_result = analyze(user_handle)
# celebrity_result = analyze(celebrity_handle)
def end_result():
    origin_FB = 'me'
    destination_FB = 'me'
    origin_twitter = 'AnthonyTPlummer'
    destination_twitter = 'tamaradhia'

    # WATSONS Analysis
    analysis = get_object_or_404(Analysis)

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

    # Getting FaceBook Profile Pic
    FBProfilePic1 = getFBprofilePic(origin_FB)
    FBProfilePic2 = getFBprofilePic(destination_FB)

    # Getting Cover Picture from Facebook
    # FBCoverPic1 = getFBCoverPic(origin_FB)
    # FBCoverPic2 = getFBCoverPic(destination_FB)

    # Creating a place to store the analyzed metric Results
    analysis.category = []
    analysis.metric = []

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
    user1_list[::2] = package1.category
    user1_list[1::2] = package1.metric


    user2_list = [None]*(len(package2.metric)+len(package2.category))
    user2_list[::2] = package2.category
    user2_list[1::2] = package2.metric

    user1_list = zip(package1.metric, package1.category)
    user2_list = zip(package2.metric, package2.category)

    #Loop to populate categories returned from Watson
    for a in data1[1]:
        package1.category.append(a)
    for a in data2[1]:
        package2.category.append(a)

    #Loop to populate metric percentages returned from Watson
    for i in data1[0]:
        package1.metric.append(i)
    for i in data2[0]:
        package2.metric.append(i)

    theproper = zip(package1.category,compare(package1.metric, package2.metric))


    if profile:

        print("")
        print("FOR FUN AND JOKES, DO NOT HATE THE PLAYER, HATE THE GAME! ")
        print("")

        similarityVeryHigh = []
        similarityMedium = []
        similarityLow = []

        for x,y in theproper:
            print("")
            print("Category: " + str(x))
            analysis.category.append(x)
            print("Metric: " + str(y))
            if y > decimal.Decimal(.52):
                print("Very High Similarity Detected for : " + str(analysis.category))
                similarityLow.append([x,y])
            if y < decimal.Decimal(.55) and y > decimal.Decimal(.22):
                print("Medium Similarity Detected for : " + str(analysis.category))
                similarityMedium.append([x,y])
            if y < decimal.Decimal(.22):
                print("Low Similarity Detected for : " + str(analysis.category))
                similarityVeryHigh.append([x,y])

    return [analysis, data1, data2, FBProfilePic1, FBProfilePic2, post1, post2, profile, similarityLow, similarityMedium, similarityVeryHigh, tweets1, tweets2, user1, user2, user1_list, user2_list]


#Flatten the results received from the Watson PI API
# user = flatten(user_result)
# celebrity = flatten(celebrity_result)

#Compare the results of the Watson PI API by calculating
#the distance between traits
# compared_results = compare(user,celebrity)

#Sort the results

getTwitterPosts(user_handle)

# Print the results to the user
# for keys, value in sorted_results[:5]:
# 	print keys ,
# 	print (user[keys]),
# 	print ('->'),
# 	print (celebrity[keys]),
# 	print ('->'),
# 	print (compared_results[keys])

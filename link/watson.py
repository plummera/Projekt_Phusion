import sys
import requests
import json
import operator
import twitter
import facebook
import requests

from datetime import datetime
from django.http import JsonResponse
from watson_developer_cloud import PersonalityInsightsV3 as PersonalityInsights
from django.utils.encoding import force_text
from django.core.serializers.json import DjangoJSONEncoder
from django.core import serializers
from .credentials import *

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

    # for post in posts['posts']['data']:
        # post['created_time'] = datetime.strptime(post['created_time'], "%d-%M-%Y")


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

    #IBM credentials
    pi_username = "0fb3b935-6c02-47d6-a502-027cf7a47b8e"
    pi_password = "m7lYTjBbpZRN"

    personality_insights = PersonalityInsights(version="2016-10-19",username=pi_username,password=pi_password)

    personality_insights.set_detailed_response(False)

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

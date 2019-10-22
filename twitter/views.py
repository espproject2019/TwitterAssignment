from django.shortcuts import render
from requests_oauthlib import OAuth1Session
import twitter
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import json
@csrf_exempt
#Developer - Jumana
def home(request):
    return render(request, 'twitter/home.html')

def order(request):
    return render(request, 'twitter/order.html')

def returnConfigKeys():
    return OAuth1Session('EggZ78mMlqzx1NRl4CiJMa1K0', 'DHONwwc67epaknGLfXQ9zkBX9DxINEuWo6PlLyvJNGqTLnBZYK',
                        '1183878543110881280-Mx3TNNHjfOKEgr6kqPELJuGJetBziq',
                        'mEFItxDycCtOSHpipqpQSRQMsPR1sx1Kmlkc89JYJf63J')
#Developer - Akshaya
def createTweet(request):
    twitter = returnConfigKeys()
    userTweet = request.GET.get('userTweet')
    print(userTweet)
    postData = {'status': userTweet}
    URL = "https://api.twitter.com/1.1/statuses/update.json"
    r = twitter.post(URL, postData)
    data = r.json()
    return HttpResponse(data['id'])


def getUserData():
	URL = "https://api.twitter.com/1.1/users/show.json"
	PARAMS = {'user_id': 256071675, 'screen_name': '_akNagarajan_'}
	r = twitter.get(url = URL, params = PARAMS)
	data = r.json()
	print(data)

#Developer - Akshaya
def get(request):
  context = RequestContext(request)
  context_dict = {}
  # Update the dictionary with csrf_token
  conext_dict.update(csrf(request))
  return render_to_response("home.html", context_dict, context)

def getUserTimeline(request):
	twitter = returnConfigKeys()
	URL = "https://api.twitter.com/1.1/statuses/user_timeline.json"
	r = twitter.get(url = URL)
	data = r.json()
	return data.status.id

#Developer - Gowri  
#to retrieve tweet by the tweet ID
def retrieveTweet(request):
    twitter = returnConfigKeys()
    tweetId = request.GET.get('tweetId')
    URL = "https://api.twitter.com/1.1/statuses/show.json?id=" + (tweetId*1)
    r = twitter.get(url = URL)
    data = r.json()
    #data1 = json.loads(data)
    tweet = data['text']

	#return render(request, 'twitter/createTweet.html')
    return HttpResponse(tweet)

#Developer - Gulya
#to retrieve tweet by the tweet ID
def deleteTweet(request):
    twitter = returnConfigKeys()
    tweetId = request.GET.get('tweetId')
    URL = "https://api.twitter.com/1.1/statuses/destroy/" + (tweetId*1) + ".json"
    r = twitter.post(URL)
    data = r.json()
    tweet = data['text']
    print('Deleted TweetID = ', data['id'])
    print('Deleted Tweet = ', tweet)
    return HttpResponse(tweet)

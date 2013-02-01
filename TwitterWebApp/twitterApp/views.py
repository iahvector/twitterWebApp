# Create your views here.
import oauth2 as oauth
import urllib
import urlparse
import logging

from django.http import HttpResponse
from django.conf import settings
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from TwitterWebApp.twitterApp.models import User

log = logging.getLogger(__name__)

consumer = oauth.Consumer(settings.CONSUMER_KEY, settings.CONSUMER_SECRET)


def index(request):
    log.debug("Logging in...")
    if 'step' not in request.session:
        log.debug("Requesting token...")
        client = oauth.Client(consumer)
        # Uncomment when on localhost.
        resp, content = client.request(settings.REQUEST_TOKEN_URL, "POST", body=urllib.urlencode({'oauth_callback': settings.LOCALHOST_URL}))
        # Uncomment when deployed on server.
        # resp, content = client.request(settings.REQUEST_TOKEN_URL, "GET")
        if resp['status'] != '200':
            print resp
            print content
            raise Exception("Invalid response from twitter!")
        else:
            print resp
            print content
            request.session['request_token'] = dict(urlparse.parse_qsl(content, keep_blank_values=True))
            request.session['step'] = "1"

        return HttpResponseRedirect(settings.AUTHORIZE_URL + "?oauth_token=" + request.session['request_token']['oauth_token'])

    elif request.session['step'] == "1":
        log.debug("Authorizing...")
        token = oauth.Token(request.session['request_token']['oauth_token'], request.session['request_token']['oauth_token_secret'])
        client = oauth.Client(consumer, token)

        # Uncomment when on localhost.
        resp, content = client.request(settings.ACCESS_TOKEN_URL, "POST", body=urllib.urlencode({'oauth_callback': settings.LOCALHOST_URL}))
        # Uncomment when deployed on server.
        # resp, content = client.request(settings.ACCESS_TOKEN_URL, "GET")
        if resp['status'] != '200':
            print resp
            print content
            del request.session['step']
            raise Exception("Invalid response from twitter!")
        else:
            log.debug("Switching to user profile...")
            print resp
            print content
            del request.session['step']
            request.session['access_token'] = dict(urlparse.parse_qsl(content, keep_blank_values=True))
            return HttpResponseRedirect(reverse('TwitterWebApp.twitterApp.views.loginByScreenName', args=(request.session['access_token']['screen_name'],)))


def loginByScreenName(request, screenName):
    log.debug("Accessing user profile...")
    try:
        user = User.objects.get(twitter_screen_name=screenName)
    except User.DoesNotExist:
        user = User(twitter_id=request.session['access_token']['user_id'], twitter_screen_name=request.session['access_token']['screen_name'], oauth_token=request.session['access_token']['oauth_token'], oauth_token_secret=request.session['access_token']['oauth_token_secret'])
        user.save()

    user = User.objects.get(twitter_screen_name=screenName)
    return HttpResponse("User ID: " + str(user.twitter_id) + "</br>" + "User name: " + user.twitter_screen_name + "</br>" + "OAuth token: " + user.oauth_token + "</br>" + "OAuth token secret: " + user.oauth_token_secret)

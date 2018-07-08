from twython import Twython, TwythonError
from secrets import *

twitter = Twython(app_key, app_secret, oauth_token, oauth_token_secret)

#Setting Twitter's search results as a variable
search_results = twitter.search(q="james baldwin", count=1, results_type='popular')
try:
    for tweet in search_results["statuses"]:
        twitter.retweet(id = tweet["id_str"])
except TwythonError:
    pass

from twython import Twython, TwythonError
from secrets import *

twitter = Twython(app_key, app_secret, oauth_token, oauth_token_secret)

#Setting Twitter's search results as a variable
search_results = twitter.search(q="james baldwin", count=20, result_type="popular")

tweet_counter=0

for tweet in search_results["statuses"]:
    try:
        if tweet['retweet_count'] > 100 and tweet_counter ==0:
            twitter.retweet(id = tweet["id_str"])
            tweet_counter +=1
    except TwythonError:
        pass

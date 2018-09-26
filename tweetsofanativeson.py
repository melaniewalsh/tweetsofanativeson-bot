from twython import Twython, TwythonError
from secrets import *

twitter = Twython(app_key, app_secret, oauth_token, oauth_token_secret)
#Setting Twitter's search results as a variable
search_results = twitter.search(q="'james baldwin'", count=100, lang="en", result_type="popular")
tweet_counter=0


def is_baldwin(status):

    test_text = ' '.join(status['text'].lower().split()) # Remove capital letters and excessive whitespace/linebreaks
    usernames = []
    if status['user']['screen_name'] not in usernames and all(u not in status['text'] for u in usernames):
        if 'james baldwin' in test_text:
            return True
        else:
            return False
    else:
        return False

for tweet in search_results["statuses"]:
    if is_baldwin(tweet):
        try:
            if tweet['retweet_count'] > 100 and tweet_counter ==0:
                twitter.retweet(id = tweet["id_str"])
                tweet_counter +=1
            elif tweet['user']['followers_count'] > 10000 and tweet_counter ==0:
                twitter.retweet(id = tweet["id_str"])
                tweet_counter +=1
        except TwythonError as e:
            print(e)

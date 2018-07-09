from twython import Twython, TwythonError
from secrets import *

twitter = Twython(app_key, app_secret, oauth_token, oauth_token_secret)

#Setting Twitter's search results as a variable
search_results = twitter.search(q="james baldwin", count=10, result_type="popular")

def is_baldwin(status):
    """
    Determines whether or not the tweet is a William Carlos Williams parody,
    using the same list of queries that the streaming API uses.
    """
    test_text = ' '.join(status['text'].lower().split()) # Remove capital letters and excessive whitespace/linebreaks
    usernames = [] # Block screen_names of known parody accounts
    if status['user']['screen_name'] not in usernames and all(u not in status['text'] for u in usernames):
        if 'james baldwin' in test_text: # Capture parodies of the form
            return True
        #elif 'plums' in test_text and 'icebox' in test_text:
            #return True
        else:
            return False
    else:
        return False

tweet_counter=0

for tweet in search_results["statuses"]:
    try:
        if tweet['retweet_count'] > 100 and tweet_counter ==0:
            twitter.retweet(id = tweet["id_str"])
            tweet_counter +=1
    except TwythonError:
        pass

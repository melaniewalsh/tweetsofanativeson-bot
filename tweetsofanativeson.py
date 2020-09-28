from twython import Twython, TwythonError
from secrets import *
from datetime import datetime


#Initialize Twitter bot
twitter_bot = Twython(app_key, app_secret, oauth_token, oauth_token_secret)

#Collect the most popular tweets that mention James Baldwin
search_results = twitter_bot.search(q="'james baldwin'", count=100, lang="en", result_type="mixed")

#Tweet counter to make sure that the bot only retweets one tweet every time the script runs
tweet_counter=0

#Establish today's date
todays_date = datetime.strftime(datetime.now(), '%Y-%m-%d')

#Function to make sure tweet mentions "James Baldwin"
def mentions_baldwin(status):
    # Remove capital letters and excessive whitespace/linebreaks
    test_text = ' '.join(status['text'].lower().split()) 
    #usernames = []
    #if status['user']['screen_name'] not in usernames and all(u not in status['text'] for u in usernames):
    if 'james baldwin' in test_text:
        return True
    else:
        return False

#Loop through search results
for tweet in search_results["statuses"]:
    
    if 'retweeted_status' in tweet.keys():
        tweet_date = tweet['retweeted_status']['created_at']
        followers_count = tweet['retweeted_status']['user']['followers_count']
        rt_count = tweet['retweeted_status']['retweet_count']
    else:
        tweet_date = tweet['created_at']
        followers_count = tweet['user']['followers_count']
        rt_count = tweet['retweet_count']
    #Reformat date of tweet    
    tweet_date = datetime.strptime(tweet_date,'%a %b %d %H:%M:%S +0000 %Y')
    tweet_date = datetime.strftime(tweet_date,'%Y-%m-%d')
    
    if tweet_date == todays_date:
        if mentions_baldwin(tweet) == True:
            try:
                #Check that tweets has more than 100 RTs
                if  rt_count > 100 and tweet_counter ==0:
                    #Retweet the tweet!
                    twitter_bot.retweet(id = tweet["id_str"])
                    tweet_counter +=1
                    print(f"✨Met RT threshold✨ Succesfully retweeted {tweet['text']}!")
                #Check that Twitter account has more than 1000 followers
                elif  followers_count > 10000 and tweet_counter ==0:
                        #Retweet the tweet!
                        twitter_bot.retweet(id = tweet["id_str"])
                        tweet_counter +=1
                        print(f"✨Met follower threshold✨ Succesfully retweeted {tweet['text']}!")
            except TwythonError as e:
                print(e)
                print(tweet['text'], followers_count, rt_count)

# import tweepy
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler, API
from tweepy import Stream, streaming, Cursor
from textblob import TextBlob
import math
import time
import json

consumer_key = ''
consumer_secret = ''

access_token = ''
access_token_secret = ''

#*****TWITTERCLIENT
class TwitterClient(object):

    """
    Class for take user timeline tweets
    """

    def __init__(self, twitter_user=None):

        self.auth = Autorization().auto()
        self.client = API(self.auth)

        self.twitter_user = twitter_user

    def get_user_timeline_tweets(self, tweets_number):

        tweets = []

        for tweet in Cursor(self.client.user_timeline, id=self.twitter_user).items(tweets_number):
            tweets.append(tweet)

        return tweets

    def get_friend_list(self, friend_number):

        friends = []

        for friend in Cursor(self.client.friends).items(friend_number):
            friends.append(friend)

        return friends

    # Get first "tweets_number" tweets on your newspage(wall)
    def get_homeline_tweets(self, tweets_number):

        tweets = []

        for  tweet in Cursor(self.client.home_timeline).items(tweets_number):
            tweets.append(tweet)

        return tweet

#*****AUTORIZATION
class Autorization():

    """
    Class fo autorization
    """

    def auto(self):

        auth = OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        return auth


#*****TWITTERSTREAMER
class TwitterStreamer():

    """
    Base class wich init file and tags
    and start to stream tweets
    """

    def __init__(self, file_name, tags_name):

        self.file_name = file_name
        self.tags_name = tags_name
        self.auth = Autorization().auto()

    def stream_tweets(self):
        # Connect to twitter API

        # Init my listener
        listener = StdOutListener(self.file_name)

        # Start striming, with filter(word what need to be in tweet)
        stream = Stream(self.auth, listener)
        stream.filter(track=self.tags_name)


#*****STDOUTLISTENER
class StdOutListener(StreamListener):

    """
    Simple listener wich steam tweets and if is no error
    save it in file
    """


    #init variables for catch 420
    def __init__(self, file_name, path=None):
        self.path = path
        self.siesta = 0
        self.nightnight = 0
        self.fetched_tweets_filename = file_name

    # Working with data func
    def on_data(self, raw_data):

        # If has no errors print data and save it to file
        try:
            print(raw_data)
            with open(self.fetched_tweets_filename, 'a') as file:
                file.write(raw_data)
            # comment for test
            # return True
        except BaseException as error:
            print("The error is: ", str(error))
        # For test we take only one tweet
        return True

    # If error func
    def on_error(self, status_code):
        print(status_code)
        # If error is 420(to many requests), we will sleep and take a time for reload
        if status_code == 420:
            sleepy = 60 * math.pow(2, self.siesta)
            print(time.strftime("%Y%m%d_%H%M%S"))
            print( "A reconnection attempt will occur in " + \
                    str(sleepy / 60) + " minutes.")
            time.sleep(sleepy)
            self.siesta += 1
            # exit if Rate Limiting
            return False
        return True

    # Except re-tweets
    def on_status(self, status):
        if status.retweeted_status:
            return
        print(status)


if __name__ == '__main__':

    file_name = 'data.json'
    tags_name = ['Poroshenko']

    # twitter_streamer = TwitterStreamer(file_name, tags_name)
    # twitter_streamer.stream_tweets()

    twitter_client = TwitterClient(twitter_user='OneRepublic')

    print(twitter_client.get_user_timeline_tweets(1))

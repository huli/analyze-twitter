import tweepy
import json

class TwitterStreamListener(tweepy.StreamListener):
    def __init__(self, api=None, number_of_tweets = 100):
        super(TwitterStreamListener, self).__init__()
        self.num_tweets = 0
        self.number_of_tweets = number_of_tweets
        self.file = open("tweets.txt", "w")

    def on_status(self, status):
        tweet = status._json
        self.file.write( json.dumps(tweet) + '\n' )
        self.num_tweets += 1
        if self.num_tweets <= self.number_of_tweets:
            return True
        else:
            return False
        self.file.close()

    def on_error(self, status):
        print(status)
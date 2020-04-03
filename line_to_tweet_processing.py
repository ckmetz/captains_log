import tweepy
from credentials import *


# Access and auth our twitter credentials
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

def split_line(line, tweets = None):
    tweets = tweets if tweets else []

    if len(line) < 140:
        tweets.append(line)
        return tweets

    sub_str = line[0:140]
    last_space_idx = sub_str.rfind(' ')
    if int(last_space_idx) > 0:
        new_line = line[last_space_idx + 1:]
        tweets.append(sub_str[0:last_space_idx])
        if len(new_line) > 0:
            split_line(new_line, tweets)

    return tweets

def send_tweets(tweets):
    is_parent_tweet = True
    parent_tweet_id = 0
    for tweet in tweets:
        if is_parent_tweet:
            tweet = api.update_status(tweet)
            parent_tweet_id = tweet.id
            is_parent_tweet = False
        else:
            tweet = api.update_status(tweet, parent_tweet_id, True)
            parent_tweet_id = tweet.id


def send_file_line_as_tweets(line):
    tweets = []
    if len(line) >= 140:
        tweets = split_line(line)
    else:
        tweets.append(line)
    send_tweets(tweets)


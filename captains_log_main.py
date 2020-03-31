# Import credentials
import tweepy
from time import sleep
from credentials import *


def split_tweet(line, tweets = None):
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
            split_tweet(new_line, tweets)

    return tweets


# Access and auth our twitter credentials
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


# Open file for reading
log_file = open('log_data/log_data_personal_picard.txt', 'r')
# Read file lines into a list
log_file_lines = log_file.readlines()
# Close file
log_file.close()

for line in log_file_lines:
    if line !='\n':
        if len(line) <= 140:
            api.update_status(line)
        else:
            tweets = split_tweet(line)
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
        sleep(120)



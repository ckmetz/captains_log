# Import credentials
from credentials import *

# Access and auth our twitter credentials
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


# Open file for reading
log_file = open('log_data_personal_picard.txt', 'r')

# Read file lines into a list
log_file_lines = log_file.readlines()

# Close file
log_file.close()


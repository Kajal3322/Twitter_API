import unicodedata
import tweepy
import csv
import configparser

# read configs

config = configparser.ConfigParser()
config.read('config.ini')

api_key = config['twitter']['api_key']
api_key_secret = config['twitter']['api_key_secret']
access_token = config['twitter']['access_token']
access_token_secret = config['twitter']['access_token_secret']

#print(api_key)
#print(api_key_secret)
#print(access_token)
#print(access_token_secret)


# Authenticate to Twitter
auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)

# Create API object
api = tweepy.API(auth)

# Define the username of the twitter account
username = "elonmusk"

# Get all tweets for the user
all_tweets = []
new_tweets = api.user_timeline(screen_name=username, count=200)
all_tweets.extend(new_tweets)
oldest_id = all_tweets[-1].id - 1

# Continue to get tweets until there are no more tweets to get
while len(new_tweets) > 0:
    new_tweets = api.user_timeline(screen_name=username, count=200, max_id=oldest_id)
    all_tweets.extend(new_tweets)
    oldest_id = all_tweets[-1].id - 1

# Create a list of dictionaries containing tweet information
tweet_data = []
for tweet in all_tweets:
    tweet_dict = {
        "Creation Date": tweet.created_at,
        "Text": tweet.text,
        "Favorite Count": tweet.favorite_count,
        "Retweet Count": tweet.retweet_count
    }
    tweet_data.append(tweet_dict)


# Save tweet data to a CSV file
with open("elonmusk_tweets.csv", "w", encoding ='utf-8' , newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["Creation Date", "Text", "Favorite Count", "Retweet Count"])
    writer.writeheader()
    writer.writerows(tweet_data)




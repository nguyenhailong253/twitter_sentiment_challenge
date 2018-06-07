import tweepy
from textblob import TextBlob

# Step 1 - Authenticate

consumer_key= 'CONSUMER_KEY_HERE'
consumer_secret= 'CONSUMER_SECRET_HERE'

access_token='ACCESS_TOKEN_HERE'
access_token_secret='ACCESS_TOKEN_SECRET_HERE'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#Step 2 - Define labelling function

def label (analysis, threshold = 0):
    if analysis.sentiment [0] > threshold:
        return 'Positive'
    else:
        return 'Negative'
    
#Step 3 - Retrieve Tweets
public_tweets = api.search('Infinity War')

#Step 4 Perform Sentiment Analysis on Tweets and write to csv file
with open('InfinityWarTweet.csv', 'w') as file:
    file.write("tweet, sentiment_label\n")
    for tweet in public_tweets:
        analysis = TextBlob(tweet.text)
        file.write('%s,%s\n' %(tweet.text.encode('utf8'), label(analysis)))




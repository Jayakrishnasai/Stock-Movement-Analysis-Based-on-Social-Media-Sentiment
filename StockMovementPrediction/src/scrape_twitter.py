import tweepy
import pandas as pd

# Twitter API credentials (provided by you)
API_KEY = 'YOUR_API_KEY'
API_SECRET = 'YOUR_API_SECRECT'
ACCESS_TOKEN = 'YOUR_ACCESS_TOKEN'
ACCESS_TOKEN_SECRET = 'YOUR_ACCESS_TOKEN_SECRET'

# Authenticate to Twitter
auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

def scrape_tweets(keyword, max_tweets=100):
    """Scrape tweets based on a keyword."""
    tweets = tweepy.Cursor(api.search_tweets, q=keyword, lang="en").items(max_tweets)
    data = [{"Tweet": tweet.text, "Created_At": tweet.created_at} for tweet in tweets]
    return pd.DataFrame(data)

# Scrape Data
df = scrape_tweets("stock market", max_tweets=200)

# Save Data
df.to_csv("../data/tweets.csv", index=False)
print("Tweets scraped and saved!")

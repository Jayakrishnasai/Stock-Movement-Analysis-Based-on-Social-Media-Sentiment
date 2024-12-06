import tweepy
import pandas as pd

# Twitter API credentials (provided by you)
API_KEY = 'pBZjUuK804PESg2ohvzeOkNnk'
API_SECRET = 'a7erOK8jvhQhJP5RD0oZp3npugnYgdYm3lsT0eWoR1ncU6rKXB'
ACCESS_TOKEN = '1480163519546884100-GZb6Ht2rajcCqqK8ahcsyKAooMx9ks'
ACCESS_TOKEN_SECRET = 'iEImL15o0AgIgJZFgnkzVhV6rA2Csq1ug7ijA2jCLaPAC'

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
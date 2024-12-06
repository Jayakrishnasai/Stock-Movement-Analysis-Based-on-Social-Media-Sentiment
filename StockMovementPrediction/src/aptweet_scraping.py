import tweepy
import pandas as pd
import time

# Your Twitter API V2 credentials
bearer_token = 'AAAAAAAAAAAAAAAAAAAAADSPxQEAAAAAeFzr66XIehSUXzXOofNgK7XjIpQ%3DyDXbvL6E60vqA7SU5CN3fdjHbvsJjfSubf3zUMjeE24yL3oKhz'

# Initialize Tweepy client for API V2
client = tweepy.Client(bearer_token=bearer_token)

# Search for tweets related to "stock market"
query = "stock market -is:retweet"  # Excluding retweets

# Initialize an empty list to store tweet data
tweets_data = []

# Define the number of tweets you want to collect
max_tweets = 500
max_results_per_request = 100  # The max limit per request
tweet_count = 0

# Pagination: Handle rate limits and pagination of results
while tweet_count < max_tweets:
    try:
        # Fetch recent tweets (max 100 per request)
        tweets = client.search_recent_tweets(query=query, max_results=max_results_per_request)
        
        # Store tweet data
        for tweet in tweets.data:
            tweets_data.append({"text": tweet.text, "created_at": tweet.created_at})
            tweet_count += 1
        
        # If we've collected enough tweets, break out of the loop
        if tweet_count >= max_tweets:
            break
        
        # Wait for 1 second to avoid rate limit issues
        time.sleep(1)
    
    except tweepy.TooManyRequests:
        # Wait for the rate limit window to reset (15 minutes)
        print("Rate limit exceeded. Sleeping for 15 minutes...")
        time.sleep(15 * 60)

# Create a DataFrame with collected tweet data
df = pd.DataFrame(tweets_data)

# Save DataFrame to CSV
df.to_csv("tweets_output.csv", index=False)

print(f"{tweet_count} tweets saved to CSV successfully!")

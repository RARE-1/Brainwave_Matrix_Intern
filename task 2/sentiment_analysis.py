import tweepy
import re
from textblob import TextBlob
import matplotlib.pyplot as plt

# Tweeter's Bearer token
BEARER_TOKEN = 'AAAAAAAAAAAAAAAAAAAAAEs9wgEAAAAAAUGohGhEUzNaY%2FboQ6ZPuubxeC0%3DhHuNfSWrLeYkPnWouZCenG9QWR2RZmhMQ5FZeIzlCw8EVJ0bPT'

# Authenticate 
client = tweepy.Client(bearer_token=BEARER_TOKEN)

def get_tweets_v2(keyword):
    query = f"{keyword} -is:retweet lang:en"
    tweets = client.search_recent_tweets(query=query, max_results=100, tweet_fields=['created_at', 'text'])
    return [tweet.text for tweet in tweets.data]

def clean_text(text):
    text = re.sub(r'http\S+', '', text)  
    text = re.sub(r'@\w+', '', text)     
    text = re.sub(r'#\w+', '', text)     
    text = re.sub(r'\W', ' ', text)      
    return text.lower()                  

def analyze_sentiment(text):
    analysis = TextBlob(text)
    return analysis.sentiment.polarity

def plot_sentiment(dates, sentiment_scores):
    plt.plot(dates, sentiment_scores)
    plt.xlabel('Date')
    plt.ylabel('Sentiment Score')
    plt.title('Sentiment Trend Over Time')
    plt.show()

# Example usage
keyword = 'Python'
tweets = get_tweets_v2(keyword)

# Debug 
print("Tweets fetched:", tweets)  

if tweets:  
    cleaned_tweets = [clean_text(tweet) for tweet in tweets]
    print("Cleaned tweets:", cleaned_tweets)  

    sentiment_scores = [analyze_sentiment(tweet) for tweet in cleaned_tweets]
    print("Sentiment scores:", sentiment_scores)  

    # dates for plotting
    dates = ['2024-10-01'] * len(sentiment_scores)

    plot_sentiment(dates, sentiment_scores)
else:
    print("No tweets fetched. Please check the keyword.")

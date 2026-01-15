import tweepy
import time

# -----------------------------
# 1. TWITTER API AUTHENTICATION
# -----------------------------

API_KEY = "YOUR_API_KEY"
API_SECRET = "YOUR_API_SECRET"
ACCESS_TOKEN = "YOUR_ACCESS_TOKEN"
ACCESS_TOKEN_SECRET = "YOUR_ACCESS_TOKEN_SECRET"

auth = tweepy.OAuth1UserHandler(
    API_KEY, API_SECRET,
    ACCESS_TOKEN, ACCESS_TOKEN_SECRET
)

api = tweepy.API(auth)

# -----------------------------
# 2. POST A TWEET AUTOMATICALLY
# -----------------------------

def post_tweet(message):
    try:
        api.update_status(message)
        print("Tweet Posted!")
    except Exception as e:
        print("Error:", e)

# Example:
post_tweet("Hello world, this is a test tweet from my Python bot!")

# -----------------------------
# 3. AUTO-LIKE TWEETS BY KEYWORD
# -----------------------------

def auto_like(keyword, limit=5):
    for tweet in tweepy.Cursor(api.search_tweets, q=keyword).items(limit):
        try:
            tweet.favorite()
            print(f"Liked tweet from @{tweet.user.screen_name}")
            time.sleep(2)
        except Exception as e:
            print("Error:", e)

# Example:
# auto_like("python programming")

# -----------------------------
# 4. AUTO-FOLLOW USERS
# -----------------------------

def auto_follow(keyword, limit=5):
    for tweet in tweepy.Cursor(api.search_tweets, q=keyword).items(limit):
        try:
            tweet.user.follow()
            print(f"Followed @{tweet.user.screen_name}")
            time.sleep(2)
        except Exception as e:
            print("Error:", e)

# Example:
# auto_follow("tech news")


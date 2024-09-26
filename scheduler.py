import time
import os
from dotenv import load_dotenv
from utils import post_to_twitter, post_to_facebook

# Load credentials from .env file
load_dotenv()

TWITTER_USERNAME = os.getenv("TWITTER_USERNAME")
TWITTER_PASSWORD = os.getenv("TWITTER_PASSWORD")
FACEBOOK_USERNAME = os.getenv("FACEBOOK_USERNAME")
FACEBOOK_PASSWORD = os.getenv("FACEBOOK_PASSWORD")

# Sample post content and schedule
posts = [
    {"platform": "twitter", "content": "Hello Twitter!", "time": 10},  # Time in seconds
    {"platform": "facebook", "content": "Hello Facebook!", "time": 20},
]

def schedule_posts():
    for post in posts:
        if post["platform"] == "twitter":
            post_to_twitter(TWITTER_USERNAME, TWITTER_PASSWORD, post["content"])
        elif post["platform"] == "facebook":
            post_to_facebook(FACEBOOK_USERNAME, FACEBOOK_PASSWORD, post["content"])
        time.sleep(post["time"])

if __name__ == "__main__":
    schedule_posts()

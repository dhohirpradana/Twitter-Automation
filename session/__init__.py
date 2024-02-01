import os
from datetime import datetime, timedelta

import tweepy

from dotenv import load_dotenv
load_dotenv()

API_KEY = os.environ.get("TWITTER_API_KEY")
API_SECRET = os.environ.get("TWITTER_API_SECRET")
ACCESS_TOKEN = os.environ.get("TWITTER_ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.environ.get("TWITTER_ACCESS_TOKEN_SECRET")
NODEMAVEN_PROXY = os.environ.get("NODEMAVEN_PROXY")

# validate
if not API_KEY:
    raise ValueError("API_KEY is not set")
if not API_SECRET:
    raise ValueError("API_SECRET is not set")
if not ACCESS_TOKEN:
    raise ValueError("ACCESS_TOKEN is not set")
if not ACCESS_TOKEN_SECRET:
    raise ValueError("ACCESS_TOKEN_SECRET is not set")
if not NODEMAVEN_PROXY:
    raise ValueError("PROXY is not set")


def create_session():
    print("Creating session...")
    try:
        # authentication
        auth = tweepy.OAuth1UserHandler(API_KEY, API_SECRET)
        auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

        # create session with node maven proxy
        api = tweepy.API(auth=auth, proxy=NODEMAVEN_PROXY)

        return api
    except Exception as e:
        print(e)
        raise e

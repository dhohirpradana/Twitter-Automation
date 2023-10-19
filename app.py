import os
from datetime import datetime, timedelta

import tweepy
import random
import time

api_key = os.environ.get("TWITTER_API_KEY")
api_secret = os.environ.get("TWITTER_API_SECRET")
access_token = os.environ.get("TWITTER_ACCESS_TOKEN")
access_token_secret = os.environ.get("TWITTER_ACCESS_TOKEN_SECRET")

# authentication
auth = tweepy.OAuthHandler(api_key, api_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

indonesian_months = (
    "Januari",
    "Februari",
    "Maret",
    "April",
    "Mei",
    "Juni",
    "Juli",
    "Agustus",
    "September",
    "Oktober",
    "November",
    "Desember",
)


def update_name():
    d = datetime.now()
    d_gmt_plus_7 = d + timedelta(hours=7)

    d_dd_month_yyyy = d_gmt_plus_7.strftime("%d %B %Y")

    d_indonesia = d_dd_month_yyyy.replace(
        d_gmt_plus_7.strftime("%B"),
        indonesian_months[int(d_gmt_plus_7.strftime("%m")) - 1],
    )

    # twitter_icon = ""
    calendar_emoticon = "🗓️"

    name = calendar_emoticon + " " + d_indonesia
    api.update_profile(name=name)


def update_status(text):
    api.update_status(status=text)


def get_tweet_and_retweet():
    # Search for tweets (you can customize the query)
    search_query = "Teknologi"
    tweet_count = 10  # Number of tweets to retrieve

    tweets = api.search_tweets(q=search_query, kwargs={"count": tweet_count})

    # Generate a random number between 0 and 9 (inclusive)
    random_number = random.randint(0, 9)

    # Iterate through the tweets and retweet them
    for i, tweet in enumerate(tweets):
        if i == random_number:
            try:
                tweet_id = tweet.id
                api.retweet(tweet_id)
                print(f"Retweeted: {tweet.text}")
            except tweepy.TweepError as e:
                print(f"Error: {e}")


def update_banner():
    days = ("senin", "selasa", "rabu", "kamis", "jumat", "sabtu", "minggu")
    now = datetime.now()

    now_indonesia = now + timedelta(hours=7)

    # get day
    day = days[now_indonesia.weekday()]
    print("hari: ", day)
    api.update_profile_banner(day + ".jpg")
    
def new_year():
    # Define the current date
    current_date = datetime.now()

    # Define the target date for New Year (January 1 of the next year)
    new_year_date = datetime(current_date.year + 1, 1, 1)

    # Calculate the difference between the two dates
    remaining_days = (new_year_date - current_date).days
    
    # Calculate the year for the next year
    next_year = current_date.year + 1
    
    text = f"{remaining_days} hari lagi menuju {next_year}"
    update_status(text)


if __name__ == "__main__":
    # Calculate a random delay between 3 and 7 seconds
    delay_seconds = random.randint(3, 7)
    
    # getTweetAndRetweet()
    update_name()
    
    # Delay for the random duration
    time.sleep(delay_seconds)
    
    update_banner()
    
    # new_year()

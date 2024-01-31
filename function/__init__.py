from datetime import datetime, timedelta

import random
import time
import tweepy

from session import create_session

months = (
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "Augustus",
    "September",
    "October",
    "November",
    "December",
)

api = create_session()


def update_name():
    d = datetime.now()
    # timezone gmt +7
    d_gmt_plus_7 = d + timedelta(hours=7)

    d_dd_month_yyyy = d_gmt_plus_7.strftime("%d %B %Y")

    d_indonesia = d_dd_month_yyyy.replace(
        d_gmt_plus_7.strftime("%B"),
        months[int(d_gmt_plus_7.strftime("%m")) - 1],
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
                print("Error on retweeting:", e)


def update_banner():
    days = (
        "sunday",
        "monday",
        "tuesday",
        "wednesday",
        "thursday",
        "friday",
        "saturday",
    )
    now = datetime.now()

    now_my_time = now + timedelta(hours=7)

    # if gmt -7
    # now_my_time = now - timedelta(hours=7)

    # get day
    day = days[now_my_time.weekday()]
    print("Day: ", day)
    api.update_profile_banner(f"banner/{day}.jpg")


def new_year():
    # Define the current date
    current_date = datetime.now()

    # Define the target date for New Year (January 1 of the next year)
    new_year_date = datetime(current_date.year + 1, 1, 1)

    # Calculate the difference between the two dates
    remaining_days = (new_year_date - current_date).days

    # Calculate the year for the next year
    next_year = current_date.year + 1

    text = f"{remaining_days} days left until {next_year}!"
    update_status(text)

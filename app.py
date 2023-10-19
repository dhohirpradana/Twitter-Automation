import os
from datetime import datetime, timedelta

import tweepy

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


def updateName():
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


def updateBanner():
    #days = ("senin", "selasa", "rabu", "kamis", "jumat", "sabtu", "minggu")
    now = datetime.now()

    now_indonesia = now + timedelta(hours=7)

    # get day
    day = days[now_indonesia.weekday()]
    print("hari: ", day)
    api.update_profile_banner(day + ".jpg")


if __name__ == "__main__":
    updateName()
    #updateBanner()

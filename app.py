import datetime

import tweepy

# twitter keys
api_key = "9ZviuCV1HzNYpF3gWRr1bqWLp"
api_secret = "pG9f2zyJz4nedQsoWk6xktUHm6fDHyzgr5mktgUHXnXv1V0Ex3"
access_token = "2161741-TXf87OP1LkHJfpA19m6ULUM645UYfU19eJ5iZMeRFE"
access_token_secret = "CsEHU0bmWJHhtyeZ0cljsUQK6zwKAu5g2WZxt9K68JCBl"

# authentication
auth = tweepy.OAuthHandler(api_key, api_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


# def updateName():
#     name = "A Little Coding"
#     api.update_profile(name=name)


def updateBanner():
    days=("senin","selasa","rabu","kamis","jumat","sabtu","minggu")
    now = datetime.datetime.now()
    
    # get day
    day = days[now.weekday()]
    print('day: ', day)
    api.update_profile_banner(day + ".jpg")


if __name__ == "__main__":
    # updateName()
    updateBanner()

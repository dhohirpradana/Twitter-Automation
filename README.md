# Twitter Automation Change Name and Banner

Automate change of name and Twitter profile banner using Python code and Github action.

# Steps

1. _To get Twitter Keys_
   Go to Twitter developer site [Twitter Developer](https://developer.twitter.com "Twitter Developer") and register twitter developer -> Create new project -> Create app -> Keys and token

| key name                    | description                                                                                |
| --------------------------- | ------------------------------------------------------------------------------------------ |
| TWITTER_API_KEY             | The Consumer Key for your Twitter App (this is the same for every user)                    |
| TWITTER_API_SECRET          | The Consumer Secret for your Twitter App (this is the same for every user)                 |
| TWITTER_ACCESS_TOKEN        | The Public part of an Access Token for your Twitter App (this is different for every user) |
| TWITTER_ACCESS_TOKEN_SECRET | The Secret part of an Access Token for your Twitter App (this is different for every user) |
| NODEMAVEN_PROXY             | The Secret part of an Access Token for your Twitter App (this is different for every user) |

2. _Use this template or Clone this repository and push to your Github_
   https://github.com/dhohirpradana/Twitter-Automatically-Name-Banner.git

3. _Set Github Secrets_
   Go to your repository -> Settings -> Secrets -> Action -> Set TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET, TWITTER_API_KEY, TWITTER_API_SECRET with your Twitter keys

4. (_if .github/workflows/main.yml not exists)_ _Create Workflow_
   Go to your repository -> Actions -> New workflow -> Setup a workflow yourself -> whatever.yaml

```javascript
name: twitter auto update banner and name

on:
  push:
    branches:
      - master
  schedule:
    - cron: '0 17 * * *'
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: checkout repo content
        uses: actions/checkout@v3
      - name: setup python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'

      - name: install tweepy
        run: |
          python -m pip install --upgrade pip
          pip install tweepy

      - name: execute py script # run app.py
        env:
          TWITTER_API_KEY: '${{ secrets.TWITTER_API_KEY }}'
          TWITTER_API_SECRET: '${{ secrets.TWITTER_API_SECRET }}'
          TWITTER_ACCESS_TOKEN: '${{ secrets.TWITTER_ACCESS_TOKEN }}'
          TWITTER_ACCESS_TOKEN_SECRET: '${{ secrets.TWITTER_ACCESS_TOKEN_SECRET }}'
        run: python app.py
```

5. Save

# Good Luck

[![twitter auto update banner](https://github.com/dhohirpradana/twitter-banner/actions/workflows/main.yml/badge.svg)](https://github.com/dhohirpradana/twitter-banner/actions/workflows/main.yml)

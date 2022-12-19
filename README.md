# Twitter Automatically Change Name and Banner

Automate change of name and Twitter profile banner using python and github action

# Steps
*To get Twitter Keys*
Go to Twitter developer site https://developer.twitter.com and register twitter developer -> Create new project -> Create app -> Keys and token

*Set Github Secrets*
Go to your repository -> Settings -> Secrets -> Action -> Set TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN, TWITTER_API_KEY, TWITTER_API_SECRET with your Twitter keys

*Create Workflow*
Go to your repository -> Actions -> New workflow -> Setuo a workflow yourself -> *whatever.yaml*
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
and SAVE


[![twitter auto update banner](https://github.com/dhohirpradana/twitter-banner/actions/workflows/main.yml/badge.svg)](https://github.com/dhohirpradana/twitter-banner/actions/workflows/main.yml)

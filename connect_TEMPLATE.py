import requests
from requests_oauthlib import OAuth1


def connect(ticker, date):
    oath_token=""
    oath_secret=""
    api_key=''
    secret=''

    auth = OAuth1(api_key, secret, oath_token, oath_secret)

    url = 'https://api.tradeking.com/v1/market/timesales.json?symbols={}&startdate={}&interval=5min'.format(ticker, date)

    response = requests.get(url, auth=auth).json()
    return response['response']['quotes']['quote']

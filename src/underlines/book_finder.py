#!/usr/bin/env python

import requests
import configparser
import json

config = configparser.ConfigParser()
config.read('../../config.ini')
TTB_KEY = config['DEFAULT']['TTB_KEY']


def find_blogbest_isbn13():
    response = requests.get(
        'http://www.aladin.co.kr/ttb/api/ItemList.aspx?ttbkey={}&QueryType=BlogBest&MaxResults=10&start=1&SearchTarget=Book&output=JS&Version=20131101'.format(TTB_KEY))
    isbns13 = [item.get('isbn13') for item in response.json().get('item')]
    return isbns13

def find_book(isbn13):
    response = requests.get("http://www.aladin.co.kr/ttb/api/ItemLookUp.aspx?ttbkey={}&itemIdType=ISBN13&ItemId={}&output=JS&cover=big".format(TTB_KEY, isbn13))
    book = _aladin_response_to_json(response)
    return book

def _aladin_response_to_json(response):
    json_string = response.text.strip(';')
    dict_book = json.loads(json_string)
    return dict_book['item'][0]
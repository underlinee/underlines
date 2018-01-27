#!/usr/bin/env python

import requests
import json

from underlines.common import sqltemplate, config

TTB_KEY = config.get('TTB_KEY')

def find_blogbest_isbn13():
    response = requests.get(
        'http://www.aladin.co.kr/ttb/api/ItemList.aspx?ttbkey={}&QueryType=BlogBest&MaxResults=10&start=1&SearchTarget=Book&output=JS&Version=20131101'.format(TTB_KEY))
    isbns13 = [item.get('isbn13') for item in response.json().get('item')]
    return isbns13

def find_by_isbn13(isbn13):
    response = requests.get("http://www.aladin.co.kr/ttb/api/ItemLookUp.aspx?ttbkey={}&itemIdType=ISBN13&ItemId={}&output=JS&cover=big".format(TTB_KEY, isbn13))
    book = _aladin_response_to_json(response)
    return book

def _aladin_response_to_json(response):
    json_string = response.text.strip(';').replace('\\\'', "'")
    book_dict = json.loads(json_string, strict=False)
    return book_dict['item'][0]

def init_table():
    sql = "DELETE FROM book"
    sqltemplate.execute(sql)

def get(isbn13):
    sql = "SELECT * FROM book where isbn13=%s"
    row = sqltemplate.selectone(sql, isbn13)
    return row

def save(book):
    sql = "INSERT INTO book(isbn, isbn13, title, author, publisher, cover) VALUES(%s, %s, %s, %s, %s, %s)"
    parameters = [ book['isbn'], int(book['isbn13']), book['title'], book['author'], book['publisher'], book['cover'] ]
    return sqltemplate.execute(sql, parameters)

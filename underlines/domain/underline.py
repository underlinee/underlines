#!/usr/bin/env python

from underlines.common import sqltemplate
from bs4 import BeautifulSoup

import requests

def find_underlines(isbn):
    response = requests.get("http://www.aladin.co.kr/shop/common/wbook_talktalk.aspx?ISBN={}&CommunityType=Underline".format(isbn))
    soup = BeautifulSoup(response.content, 'html5lib', from_encoding='euc-kr')
    rows = soup.find("div", {"class": "p_letter"})
    children = rows.findChildren()
    return [child.text for child in children if child.name == "tbody"]

def is_valid_underline(text):
    return text and not text.strip().isnumeric() and len(text) > 15

def save(isbn13, underline):
    sql = "INSERT INTO underline(book_id, underline) VALUES ((SELECT id from book WHERE isbn13=%s), %s)"
    parameters = [ isbn13, underline ]
    return sqltemplate.execute(sql, parameters)

def get_by_isbn13(isbn13):
    sql = "SELECT underline.* FROM underline INNER JOIN book ON book.id = underline.book_id WHERE book.isbn13=%s"
    return sqltemplate.selectone(sql, isbn13)

def get_underlines_all():
    sql = "SELECT underline FROM underline"
    results = list(sqltemplate.selectall_by_list(sql))
    return [result[0] for result in results]

def init_table():
    sql = "DELETE FROM underline"
    sqltemplate.execute(sql)
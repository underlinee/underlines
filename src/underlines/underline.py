#!/usr/bin/env python

from underlines.common import sqltemplate

def find_underlines(isbn13):
    from bs4 import BeautifulSoup
    from selenium import webdriver

    driver = webdriver.Firefox()
    driver.get("http://www.aladin.co.kr/shop/common/wbook_talktalk.aspx?ISBN={}&CommunityType=Underline".format(isbn13))
    html = driver.page_source

    soup = BeautifulSoup(html, 'html.parser')
    rows = soup.select(".p_letter > table > tbody > tr > td > div")
    underlines = [ row.text.strip() for row in rows if not row.text.strip().isnumeric() and row.text]
    return underlines

def save(isbn13, underline):
    sql = "INSERT INTO underline(book_id, underline) VALUES ((SELECT id from book WHERE isbn13=%s), %s)"
    parameters = [ isbn13, underline ]
    return sqltemplate.execute(sql, parameters)

def get_by_isbn13(isbn13):
    sql = "SELECT underline.* FROM underline INNER JOIN book ON book.id = underline.book_id WHERE book.isbn13=%s"
    return sqltemplate.selectone(sql, isbn13)

def init_table():
    sql = "DELETE FROM underline"
    sqltemplate.execute(sql)
#!/usr/bin/env python


def find_underlines(isbn13):
    from bs4 import BeautifulSoup
    from selenium import webdriver

    driver = webdriver.Firefox()
    driver.get("http://www.aladin.co.kr/shop/common/wbook_talktalk.aspx?ISBN={}&CommunityType=Underline".format(isbn13))
    html = driver.page_source

    soup = BeautifulSoup(html, 'html.parser')
    rows = soup.select(".p_letter > table > tbody > tr > td > div")
    underlines = [ row.text.strip() for row in rows if not row.text.strip().isnumeric()]
    return underlines
#!/usr/bin/env python

import logging

from underlines.domain import book, keyword, underline

log = logging.getLogger()

def collect(isbn13):
    book_dict = book.find_by_isbn13(isbn13)
    log.info("book found; title={}, isbn13={}".format(book_dict['title'], book_dict['isbn13']));

    book.save(book_dict)

    underlines = underline.find_underlines(book_dict['isbn'])
    log.info("underlines found; underlines={}, isbn13={}".format(underlines, isbn13))

    for line in underlines :
        underline_id = underline.save(book_dict['isbn13'], line)
        keywords = keyword.find_keyword(line, keyword_count=2)
        log.info("keywords found; keywords={}, underline_id={}".format(keywords, underline_id))

        for word in keywords:
            keyword.save(underline_id, word)
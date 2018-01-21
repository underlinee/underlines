#!/usr/bin/env python

from underlines import book, underline, keyword



def collect(isbn13):
    book_dict = book.find_by_isbn13(isbn13)
    book.save(book_dict)

    underlines = underline.find_underlines( book_dict['isbn13'])

    for line in underlines :
        underline_id = underline.save(book_dict['isbn13'], line)
        keywords = keyword.find_keyword(line, keyword_count=2)

        for word in keywords:
            keyword.save(underline_id, word)



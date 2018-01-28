

from underlines import collector
from underlines.common import file_reader
import time

def collect_from_isbns():
    isbns = file_reader.read_lines("isbns.txt")

    for isbn in isbns:
        try:
            collector.collect(isbn)
        except Exception as e:
            print("exception: " + isbn)
            print(e)

def update_description():
    from underlines.domain import book

    isbn13s = file_reader.read_lines("isbns.txt")

    for isbn13 in isbn13s:
        try:
            found = book.find_by_isbn13(isbn13)
            description = book.find_description(found['isbn'])
            book.update_description(found['isbn13'], description)
            time.sleep(1)
        except Exception as e:
            print("exception: " + isbn13)
            print(e)


if __name__ == "__main__":
    update_description()



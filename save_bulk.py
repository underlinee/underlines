

from underlines import collector
from underlines.common import file_reader

if __name__ == "__main__":
    isbns = file_reader.read_lines("isbns.txt")

    for isbn in isbns:
        try :
            collector.collect(isbn)
        except Exception as e:
            print("exception: " + isbn)
            print(e)


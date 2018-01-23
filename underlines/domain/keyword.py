#!/usr/bin/env python
from underlines.common import sqltemplate, config

credentials_path = config.get("GOOGLE_APPLICATION_CREDENTIALS")

def find_keyword(underline, keyword_count):
    from google.cloud import language
    from google.cloud.language import enums
    from google.cloud.language import types
    from google.oauth2 import service_account

    credentials = service_account.Credentials.from_service_account_file(credentials_path)
    client = language.LanguageServiceClient(credentials=credentials)

    document = types.Document(
        content=underline,
        type=enums.Document.Type.PLAIN_TEXT)

    response = client.analyze_entities(document=document, encoding_type=enums.EncodingType.UTF8)
    entities = _remove_duplicated_name(response.entities)
    keywords = [entity.name for entity in entities[:keyword_count] if entity.salience > 0.05]
    return keywords

def _remove_duplicated_name(entities):
    names = set()
    unique_entities = []
    for entity in entities:
        if entity.name not in names:
            unique_entities.append(entity)
            names.add(entity.name)
    return unique_entities

def save(underline_id, keyword):
    sql = "INSERT INTO keyword(underline_id, keyword) VALUES (%s, %s)"
    parameters = [ underline_id, keyword ]
    return sqltemplate.execute(sql, parameters)

def get_by_underline_id(underline_id):
    sql = "SELECT * FROM keyword WHERE underline_id=%s"
    return sqltemplate.selectone(sql, underline_id)

def get_by_isbn13(book_id):
    sql = """SELECT keyword. * FROM keyword 
                    INNER JOIN underline ON underline.id = keyword.underline_id
                    INNER JOIN book ON book.id = underline.book_id 
                    WHERE book.isbn13 = %s"""
    return sqltemplate.selectall(sql, book_id)

def init_table():
    sql = "DELETE FROM keyword"
    sqltemplate.execute(sql)
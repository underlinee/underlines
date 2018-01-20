#!/usr/bin/env python
from underlines.common import sqltemplate

def find_keyword(underline, keyword_count):
    from google.cloud import language
    from google.cloud.language import enums
    from google.cloud.language import types

    client = language.LanguageServiceClient()

    document = types.Document(
        content=underline,
        type=enums.Document.Type.PLAIN_TEXT)

    response = client.analyze_entities(document=document, encoding_type=enums.EncodingType.UTF8)
    keywords = [entity.name for entity in response.entities[:keyword_count] if entity.salience > 0.05]
    return keywords

def save(underline_id, keyword):
    sql = "INSERT INTO keyword(underline_id, keyword) VALUES (%s, %s)"
    parameters = [ underline_id, keyword ]
    return sqltemplate.execute(sql, parameters)

def get(id):
    sql = "SELECT * FROM keyword WHERE id=%s"
    return sqltemplate.selectone(sql, id)

def init_table():
    sql = "DELETE FROM keyword"
    sqltemplate.execute(sql)
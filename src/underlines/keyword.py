#!/usr/bin/env python

def find_keyword(underline, keyword_count):
    from google.cloud import language
    from google.cloud.language import enums
    from google.cloud.language import types

    client = language.LanguageServiceClient()

    document = types.Document(
        content=underline,
        type=enums.Document.Type.PLAIN_TEXT)

    response = client.analyze_entities(document=document, encoding_type=enums.EncodingType.UTF8)
    keywords = [entity.name for entity in response.entities[:keyword_count]]
    return keywords
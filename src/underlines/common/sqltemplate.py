#!/usr/bin/env python

import pymysql
from underlines.common import config

host = config.get("DB_HOST")
user = config.get("DB_USER")
password = config.get("DB_PASSWORD")
db = config.get("DB_NAME")

def selectone(sql, parameters):
    conn = pymysql.connect(host=host, user=user, password=password, db=db, charset='utf8')
    curs = conn.cursor(pymysql.cursors.DictCursor)
    curs.execute(sql, parameters)
    row = curs.fetchone()
    conn.commit()
    conn.close()
    return row

def execute(sql, parameters=None):
    conn = pymysql.connect(host=host, user=user, password=password, db=db, charset='utf8')
    curs = conn.cursor()
    if parameters is None:
        result = curs.execute(sql)
    else:
        result = curs.execute(sql, parameters)
    conn.commit()
    conn.close()
    return result

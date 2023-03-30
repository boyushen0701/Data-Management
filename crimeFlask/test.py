"""
coding: utf-8
author: tianqi
email: tianqixie98@gmail.com
"""

import pymysql
import pandas

conn = pymysql.connect(host='localhost', user='dsci551', password="dsci551", db='dsci551')
cursor = conn.cursor()
query = 'select * from LaCrime'

results = pandas.read_sql_query(query, conn)
results.to_csv("output.csv", index=False)

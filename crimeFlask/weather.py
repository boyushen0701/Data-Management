"""
coding: utf-8
author: tianqi
email: tianqixie98@gmail.com
"""
import pandas as pd
from sqlalchemy import create_engine

# Credentials to database connection
hostname = "localhost"
dbname = "dsci551"
uname = "dsci551"
pwd = "dsci551"

weatherData = pd.read_csv('weather_data.csv')
weatherDic = {'Fair': 1, 'Cloudy': 2, 'Rain': 3, 'Haze': 4, 'Smoke': 4, 'Fog': 5}
wx_phrase_label = []

for i in range(len(weatherData)):
    wx_phrase = weatherData.iloc[i]['wx_phrase']
    for key, value in weatherDic.items():
        if key in wx_phrase:
            wx_phrase_label.append(value)

weatherData['wx_phrase_label'] = wx_phrase_label

# Create SQLAlchemy engine to connect to MySQL Database
engine = create_engine("mysql+pymysql://{user}:{pw}@{host}/{db}".format(host=hostname, db=dbname, user=uname, pw=pwd))

# Convert dataframe to sql table
weatherData.to_sql('LaWeather', engine, index=False, if_exists='replace')

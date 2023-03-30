"""
coding: utf-8
author: tianqi
email: tianqixie98@gmail.com
"""

import pandas as pd
from sqlalchemy import create_engine
from math import radians, cos, sin, asin, sqrt

# Credentials to database connection
hostname = "localhost"
dbname = "dsci551"
uname = "dsci551"
pwd = "dsci551"


# calculate the distance between two points in earth
def geodistance(lng1,lat1,lng2,lat2):
    lng1, lat1, lng2, lat2 = map(radians, [float(lng1), float(lat1), float(lng2), float(lat2)])
    dlon = lng2 - lng1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    distance = 2 * asin(sqrt(a)) * 6371 * 1000
    distance = round(distance / 1000, 3)
    return distance


if __name__ == '__main__':
    data = pd.read_csv('Crime_Data_from_2020_to_Present.csv')
    cities = pd.read_csv('laCities.csv')
    columns = ['Cities', 'LAT', 'LNG']
    cities = cities[columns]

    crimetype = []
    dateList = []
    monthList = []
    dayList = []
    crimeDistrict = []
    crimeDict = {'THEFT': 1, 'STOLEN': 1, 'SEX': 2, 'RAPE': 2, 'ASSAULT': 3, 'BURGLARY': 4, \
                 'ROBBERY': 5, 'VANDALISM': 6, 'VEHICLE': 7}
    for i in range(len(data)):
        # date month, day
        date = data.iloc[i]['DATE OCC'][:10]
        month, day, year = date.split('/')
        dateList.append(year + '-' + month + '-' + day)
        monthList.append(int(month))
        dayList.append(int(day))
        # crimeType
        flag = 0
        for key, value in crimeDict.items():
            if key.lower() in data.iloc[i]['Crm Cd Desc'].lower():
                flag = 1
                crimetype.append(value)
                break
        if flag == 0:
            crimetype.append(8)
        # crimeDistrict
        minDistance = 10000
        name = ''
        lat1, lng1 = data.iloc[i]['LAT'], data.iloc[i]['LON']
        for j in range(len(cities)):
            lat2, lng2 = cities.iloc[j]['LAT'], cities.iloc[j]['LNG']
            distance = geodistance(lat1, lng1, lat2, lng2)
            if distance < minDistance:
                name = cities.iloc[j]['Cities']
                minDistance = distance
        crimeDistrict.append(name)

    data['District'] = crimeDistrict
    data['crimeType'] = crimetype
    data['date'] = dateList
    data['month'] = monthList
    data['day'] = dayList

    # Create SQLAlchemy engine to connect to MySQL Database
    engine = create_engine("mysql+pymysql://{user}:{pw}@{host}/{db}".format(host=hostname, db=dbname, user=uname, pw=pwd))

    # Convert dataframe to sql table
    data.to_sql('LaCrime', engine, index=False, if_exists='replace')
    cities.to_sql('LaCities', engine, index=False, if_exists='replace')


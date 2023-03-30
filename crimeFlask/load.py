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
uname = "root"
pwd = "Dsci-551"

# Create SQLAlchemy engine to connect to MySQL Database
engine = create_engine(
    "mysql+pymysql://{user}:{pw}@{host}/{db}".format(host=hostname, db=dbname, user=uname, pw=pwd))

# laCrime = pd.read_csv('output.csv')
# cities = pd.read_csv('laCities.csv')
# columns = ['Cities', 'LAT', 'LNG']
# cities = cities[columns]
#
# # Create SQLAlchemy engine to connect to MySQL Database
# engine = create_engine("mysql+pymysql://{user}:{pw}@{host}/{db}".format(host=hostname, db=dbname, user=uname, pw=pwd))
#
# # Convert dataframe to sql table
# laCrime.to_sql('LaCrime', engine, index=False, if_exists='replace')
# cities.to_sql('LaCities', engine, index=False, if_exists='replace')

for i in range(1, 440001, 10000):
    print(i)
    crime = pd.read_csv('output.csv', header=None, skiprows=i, nrows=10000)
    header = ['DR_NO', 'Date Rptd', 'DATE OCC', 'TIME OCC', 'AREA NAME', 'Crm Cd Desc', 'Vict Age', 'Vict Sex',
              'Vict Descent', 'Premis Desc', 'Weapon Desc', 'LOCATION', 'LAT', 'LON', 'crimeType', 'date', 'month',
              'District', 'day']
    crime.columns = header

    # Convert dataframe to sql table
    crime.to_sql('test', engine, index=False, method='multi', if_exists='append')
import sys
sys.path.append('/usr/local/lib/python2.7/site-packages/')
from pymongo import MongoClient

# sql-server (source db)
'''
sqlserver_db_config = [
  {
    'Trusted_Connection': 'yes',
    'driver': '{SQL Server}',
    'server': 'your_sql_server',
    'database': 'top_songsDB'
    'user': 'root',
    'password': 'password',
    'autocommit': True,
  }
]
'''
# mysql
mysql_db_config = [
    {
      'user': 'dariell',
      'password': 'password',
      'host': '127.0.0.1',
      'database': 'top_songsDB',
      'raise_on_warnings': True,
    }
    #Other DBs will go here
]

def mongoDB():
    client = MongoClient("localhost", 27017)
    db = client.MediumScraper
    collection = db['articles']
    cursor = collection.find({})
    return cursor

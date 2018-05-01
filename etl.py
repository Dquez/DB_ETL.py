# python modules
import mysql.connector
# import pyodbc
# import mongodb
# methods
from xl_funcs import xl_write
from mysql.connector import errorcode

def etl(query, source_cnx):
  # extract data from source db
  source_cursor = source_cnx.cursor()
  source_cursor.execute(query.extract_all)
  data = source_cursor.fetchall()
  xl_write(data, "mysql")
  source_cursor.close()
 
def etl_process(query, source_db_config, db_platform):
  # establish source db connection
  try:
    if db_platform == 'mysql':
      source_cnx = mysql.connector.connect(**source_db_config)
    
    #elif db_platform == 'mongodb':
      #source_cnx = mdb.connect(**source_db_config)
    else:
      return 'Error! unrecognized db platform'
  except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
      print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
      print("Database does not exist")
    else:
      print(err)
  print(source_cnx)

  
  etl(query, source_cnx)
  # close the source db connection
  source_cnx.close()

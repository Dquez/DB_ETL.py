# variables
from db_credentials import mysql_db_config, mongoDB
from sql_queries import mysql_queries
# methods
from etl import etl_process
from xl_funcs import xl_write

def main():
  database = raw_input("Which database would you like to scrape?")
  if database == "mongo":
   xl_write(mongoDB(), database)
  elif database == "mysql" or database == "sql":
    # mysql
    for config in mysql_db_config: 
        etl_process(mysql_queries, config, 'mysql')
  else:
    print("Sorry, that functionality hasn't been built yet!")
      
if __name__ == "__main__":
  main()

mysql_extract_all = ('''
  SELECT *
  FROM top5000
''')

mysql_extract_one = ('''
  SELECT *
  FROM top5000
  WHERE position = ?
''')

mysql_insert = ('''
  INSERT INTO `top_songsdb`.`top5000` (`position`, `artist`, `song`, `year`, `raw_total`, `raw_usa`, `raw_uk`, `raw_eur`, `raw_row`)
  VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);
''')



class MySQLQuery:
    def __init__(self, extract_all, extract_one, insert):
        self.extract_all = extract_all
        self.extract_one = extract_one
        self.insert = insert

mysql_queries = MySQLQuery(mysql_extract_all,mysql_extract_one, mysql_insert)

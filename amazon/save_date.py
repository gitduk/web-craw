import sqlite3

database_path = "database/amazon.db"
conn = sqlite3.connect("database/amazon.db", check_same_thread=False)
conn.isolation_level = None

cur = conn.cursor()
cur.execute('''CREATE TABLE  IF NOT EXISTS TopSellers (
       ASIN     CHAR(20) PRIMARY KEY NOT NULL,
       TITLE    CHAR(255) NOT NULL,
       PRICE    REAL NOT NULL,
       STARS    REAL NOT NULL,
       RATINGS  INT NOT NULL
       );
       ''')

cur.execute('''CREATE TABLE IF NOT EXISTS Reviews (
       review_id     CHAR(20) PRIMARY KEY NOT NULL,
       consumer_id   CHAR(20) NOT NULL,
       consumer_name CHAR(20) NOT NULL,
       asin          CHAR(20) NOT NULL,
       star          REAL NOT NULL,
       date          CHAR(20) NOT NULL,
       review        TEXT NOT NULL
       );
       ''')

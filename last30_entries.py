import pandas as pd
import sqlite3

conn = sqlite3.connect("playlist_radio.db")
c = conn.cursor()

#c.execute("select * from wdr2_table")

#content = c.fetchall()
db_wdr2 = pd.read_sql('select * from wdr2_table', conn)
last_entries_wdr2 = db_wdr2.tail(30)
last_entries_wdr2.to_csv("test_wdr2.csv")


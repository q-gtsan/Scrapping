import plylst-grab.py
import sqlite3

conn = sqlite3.connect("playlist_radio.db")
c = conn.cursor()

#c.execute('''CREATE TABLE wdr2(Datum as DATETIME, Song as TEXT, Interpret as TEXT)''')

wdr2_list = grab()
wdr2_df = plylstToDataFrame(wdr2_list)

wdr2_df.to_sql("wdr2_table", conn, if_exists="append", index=False)
pd.read_sql('select * from new_table_name', conn)
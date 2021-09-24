import plylst-grab.py
import sqlite3

df_test = pd.read_csv("wdr2-plylst (2).csv")
print(df_text.head())

conn = sqlite3.connect("playlist_radio.db")
c = conn.cursor()

#c.execute('''CREATE TABLE wdr2(Datum as DATETIME, Song as TEXT, Interpret as TEXT)''')

wdr2_list = grab()
wdr2_df = plylstToDataFrame(wdr2_list)

wdr2_df.to_sql("wdr2_table", conn, if_exists="append", index=False)
pd.read_sql('select * from new_table_name', conn)
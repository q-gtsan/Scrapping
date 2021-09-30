import plylst_grab as pg
import pandas as pd
import sqlite3

def into_sql():
    """Scraping Playlist and insert into database"""
    #Connect to database
    conn = sqlite3.connect("playlist_radio.db")

    #Creating a cursor for selecting
    #c = conn.cursor()

    #Creating a table with 3 columns
    #c.execute('''CREATE TABLE wdr2_table(Datum DATETIME, Song TEXT, Interpret TEXT)''')

    #grab the information and insert into sql database
    wdr2_list = pg.grab()
    wdr2_df = pg.plylstToDataFrame(wdr2_list)
    wdr2_df.to_sql("wdr2_table", conn, if_exists="append", index=True)
    #print(wdr2_df.head())
    #print(pd.read_sql('select * from wdr2_table', conn))

    conn.close()

def last_entries():
    """Export dataframe of the database table wdr2"""
    conn = sqlite3.connect("playlist_radio.db")
    c = conn.cursor()

    # c.execute("select * from wdr2_table")

    # content = c.fetchall()

    # Selecting data from table and export into a csv file
    db_wdr2 = pd.read_sql('select * from wdr2_table', conn)
    last_entries_wdr2 = db_wdr2.tail(30)
    last_entries_wdr2.to_csv("test_wdr2.csv")

    conn.close()
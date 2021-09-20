import requests
import pandas as pd
import bs4 as bs
import urllib.request
import csv
import lxml

def grab():
  """Grabbing and Returning the playlist table"""
  row = []
  source = urllib.request.urlopen("https://www1.wdr.de/radio/wdr2/musik/playlist/index.html").read()
  soup = bs.BeautifulSoup(source,'lxml')
  #Seite einlesen und Tabelle extrahieren
  
  table = soup.table
  #Tabelle abspeichern in 'table'
  
  table_rows = table.find_all('tr')
  #Tabelle-Reihen abspeichern

  for tr in table_rows:
    td = tr.find_all({'td','th'})
    for i in td:
      element = i.text.strip()
      row.append(element)
  row = row[3:]
  #relevanten Daten aus der Tabelle extrahieren
  #in row abspeichern, ersten drei Elemente beinhalten "Datum, Song, Interpret"
  #die Liste "row" in eine neu abspeichern, in der die drei Elemente nicht sind 

  return row
  #Liste "row" return

def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

def plylstToDataFrame(lst = list):
  """Returning a DataFrame with 'Date', 'Song' and 'Interpret', index is a datetime-Object already"""
  ply_lst = chunks(lst, 3)
  lst_1 = []
  for value in ply_lst:
    lst_1.append(value)
  lst_1 = sorted(lst_1)  
  ply_df = pd.DataFrame(lst_1, columns=['Datum','Song','Interpret']).set_index('Datum', drop=True)
  ply_df.index = pd.to_datetime(ply_df.index, format='%d.%m.%Y,%H.%M Uhr')
  return ply_df
  #die Playliste in ein DataFrame konvertieren und die Spalte 'Datum' als index setzen + in datetime-Object umwandeln

def load_add_save(df = pd.DataFrame):
  """Loading an existing DataFrame with 'Date', 'Song' and 'Interpret', Adding new data and saving"""
  wdr2_Obj = pd.read_csv("wdr2-plylst.csv", index_col=0)
  wdr2_Obj = wdr2_Obj.append(df)
  wdr2_Obj.to_csv("wdr2-plylst.csv")

wdr2_list = grab()
wdr2_df = plylstToDataFrame(wdr2_list)
load_add_save(wdr2_df)
print("successfulyy appended")

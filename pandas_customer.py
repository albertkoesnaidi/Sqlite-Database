import pandas as pd
import sqlite3
import folium

conn=sqlite3.connect('Ariane_Database.db')

sql='''SELECT * FROM customer; '''

df=pd.read_sql_query(sql,conn)
map=folium.Map(location=[-7.2,112], zoom_start=6)
fg=folium.FeatureGroup(name='Mymap')
#df['tanggal_pasang']=pd.to_datetime(df['tanggal_pasang'],format='%d.%m.%Y')
#x=((df['tanggal_pasang']>='2014')&(df['tanggal_pasang']<'2015'))
#x=df['tanggal_pasang']>='2020'
#print(df.loc[x])
#count=0
#for i in df.loc[x].sum(axis=1):
#    count+=1
#print(count)
x=df.koordinat.to_list()
y=[list (a) for a in (s.split(",") for s in x)]

for i in y:
    fg.add_child(folium.Marker(location=i,icon=folium.Icon(color="green")))



#for i in y:
#    print(float(i[0]))
#lat=[float(i[0]) for i in y]
#long=[float(i[1]) for i in y]
#cor=zip(lat, long)
#print(list(cor))
    
#loc=df["koordinat"].to_list()
#x=[list (a) for a in (s.split(",") for s in loc)]
#y=[float(x[0][0]),float(x[0][1])]
#print(y)

map.add_child(fg)
map.save("Map1.html")

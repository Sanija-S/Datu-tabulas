import sqlite3
# pieslēdzamies datu bāzze vai izveidojam datu bāzes failu
conn=sqlite3.connect("pavasaris.db")

# izveidojam kursoru....c- objekts pieslēgumā
c=conn.cursor #rindinu pec rindinas par bauda savienojumu ar datu bāzi



# izveidot tabulu

c.execute('''CREATE TABLE IF NOT EXISTS tabula2(
          id INTEGER PRIMARY KEY, 
          krasa TEXT.
          pilseta TEXT 
) ''') # tākā jāizpilda komandas kas  nav pitona- tam nolukam izmantojam trīs ķepiņas





#saglabāt izmaiņas....aizvērt savienojumu
conn.commit()
conn.close()

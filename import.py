import sqlite3
import pandas as pd
import pandas.io.sql as psql

# sqlite3に接続
con = sqlite3.connect('npbdb')
con2 = sqlite3.connect('db.sqlite3')
cur = con2.cursor()

# TABLE作成
#cur.execute('DROP TABLE pitchingdata')
#cur.execute('CREATE TABLE pitchingdata (kyusyumark,numberofpitch,balltype,ballspeed,result,course,first,second,third,hometeam,visitorteam,pitcher,batter,time,B,S,O,hit,walk,out,strikeout)')

df = psql.read_sql('select * from pitchingdata;', con)
df.head(10).to_sql('blog_pitchingdata',con2, if_exists='append', index=None)
df2  = psql.read_sql('select * from blog_pitchingdata;', con2)

print(df2)

con2.commit()
con.close()
con2.close()

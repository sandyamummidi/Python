import pyodbc
conn=pyodbc.connect('Driver={SQL Sever};'
                    'Server=LP-PF2835K3\SQLEXPRESS;'
                    'Database=FileSearchResults;'
                    'Trusted_Connection=yes;')
cursor=conn.cursor()
cursor.execute('''
                INSERT INTO FileSearchResults_table(File_Location,SearchCount,Nameoffile)
               VALUES
               ('C:\sandy\star.txt',1,'durga.txt'),
               ('C:\chinnu\chinni',3,'moon.txt')
               ''')



conn.commit();
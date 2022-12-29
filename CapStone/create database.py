import pyodbc
server='HCL-02-78\SQLEXPRESS'
database='DetailsofEmployee'
username='Capstone'
password='Capstone@123'
cnxn=pyodbc.connect(
       'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username +';PWD='+ password)
cursor=cnxn.cursor()
class EmployeeSchema:
    def Emp_table(self):

        query1 = cursor.execute(
            """ use DetailsofEmployee"""
           )
        '''query2 = cursor.execute("""
                 create table DetailsofEmployee_table3
                 (
                 Name varchar(50),
                 project varchar(50),
                 salary int,     
                 )"""
                 )'''
        query2=cursor.execute(''' insert into DetailsofEmployee_table3(Name,project,salary)
                                values('sandy','c++',500000)'''  )
        query=cursor.execute(''' insert into DetailsofEmployee_table3(Name,project,salary)
                                values('sam','java',90000)'''  )
        query3 = cursor.execute("""select * from DetailsofEmployee_table3""")
        cnxn.commit()
        print("Table is created")

obj=EmployeeSchema()
obj.Emp_table()



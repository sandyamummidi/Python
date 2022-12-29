import pyodbc
server = 'HCL-02-78\SQLEXPRESS'
database = 'EmployeesDetails'
username = 'capstone'
password = 'Capstone@123'
cnxn=pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username +';PWD='+ password)
cursor=cnxn.cursor()

class employee_schema:
    def employe_detailstable(self):
         try:
            query1 = cursor.execute('''use EmployeesDetails''')
            query2 = cursor.execute('''create table EmployeesDetails_table
                                               (
                                               Emp_Id int NOT NULL,
                                               Name varchar(50),
                                               project varchar(50)
                                               salary int,
                                                
                                              
                                              
                                               primary key (Emp_Id)
                                               )
                                               ''')
            query3 = cursor.execute('''select * from EmployeesDetails_table''')
            cnxn.commit()
         except:
            print("Table created sucessfully")
obj=employee_schema()
obj.employe_detailstable()
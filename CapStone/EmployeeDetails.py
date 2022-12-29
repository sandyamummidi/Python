import EmployeeDetailsDatabase
import pyodbc
server = 'HCL-02-78\SQLEXPRESS'
database = 'EmployeesDetails'
username = 'capstone'
password = 'Capstone@123'
cnxn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
cursor = cnxn.cursor()
class Existing(Exception):
    pass
class Not_in_Range(Exception):
    pass
class Employee_data:
    Bonus=2
    Projects=['Python','C','Java']
    def __init__(self,Emp_Id,Name,Project,Salary):
        self.Emp_Id = Emp_Id
        self.Name=Name
        self.Project = Project
        self.Salary=Salary


    def insert_values_in_table(self):
        try:
            query = '''  
                            insert into EmployeesDetails_table (Emp_Id,Name,Project, Salary)
                            Values
                            ('{0}',{1},'{2}',{3})  '''

            insertQuery = query.format(self.Emp_Id,self.Name, self.Project,self.Salary)
            cursor.execute(insertQuery)
            cnxn.commit()
            print("1 row inserted")
        except:
            print("Primary key not accept the same values")
    def Update_Salary(self,New_Salary,Name):
        try:
            self.New_Salary = New_Salary
            self.Name=Name
            if self.New_Salary != self.Salary:
                fileinfoQuery = '''
                                                Update EmployeesDetails_table SET Salary ='{0}' WHERE Name = '{1}'
                                                '''
                updateQuery = fileinfoQuery.format(New_Salary,self.Name)
                cursor.execute(updateQuery)
                cursor.commit()
            else:
                raise Existing
        except Existing:
            print("No Change in Salary")
    def Add_Bonus(self,bonus,Name):
        self.bonus=bonus
        self.Name=Name
        try:
            if self.bonus not in range(1,self.Bonus+1):
                raise Not_in_Range
            else:
                self.Salary=self.Salary+self.Salary*self.bonus
                Query = '''
                        Update EmployeesDetails_table SET Salary ='{0}' WHERE Name = '{1}'
                                                                '''
                updateQuery = Query.format(self.Salary, self.Name)
                cursor.execute(updateQuery)
                cursor.commit()
        except Not_in_Range:
            print("Bonus is Not Range")
    def Change_Project(self,project,Name):
        self.project=project
        self.Name=Name

        if self.project in self.Projects:
            if self.project == self.Project:
                print("Project is Already exists")
            else:
                Query = ''' Update EmployeesDetails_table SET Project ='{0}' WHERE Name = '{1}' '''
                updateQuery = Query.format(project, Name)
                cursor.execute(updateQuery)
                cursor.commit()
        else:
            print("Project is not in list")
    def Display_details(self):
        query=''' select * from EmployeesDetails_table WHERE Name='{0}' '''
        query1=query.format(self.Name)
        values=cursor.execute(query1)
        for details in values:
            print("Name:{0} salary:{1} project:{2}".format(details.Emp_Id,details.Name ,details.Project,details.Salary))
    def Delete_Employee_table(self):
       Query = ''' delete from EmployeesDetails_table where Name='sandhya'  '''
       cursor.execute(Query)
       cursor.commit()
       print("Employee has been deleted")

obj1=Employee_data(1,'sandhya','c',60000)
obj1.insert_values_in_table()
obj= EmployeeDetailsDatabase.employee_schema()
obj.employe_detailstable
obj1.insert_values_in_table()
obj1.Update_Salary(50000,'sandhya')
obj1.Add_Bonus(1,'sandhya')
obj1.Change_Project('C','SQL')
obj1.Display_details()
obj1.Delete_Employee_table()
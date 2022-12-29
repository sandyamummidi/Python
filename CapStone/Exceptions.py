#Exception handling by using class(06-Dec-2022)
class Cal:
    def div(self,input1,input2):
        return input1,input2

    try:
            input1=int(input("Enter the value1:"))
            input2=int(input("Enter the value2:"))

            #div(input1,input2)
            output=input1/input2
            print(output)

    except ZeroDivisionError:
              print("denominator is zero")
    except ValueError:
            print("value should be a number")
Obj=Cal()

#Bank programming by using exception handling
class Bank:
    def Balance(self):









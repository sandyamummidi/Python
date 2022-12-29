#check if the first three characters of a string are same or not
a=input("enter the string1")
b=input("enter the string2")
if(a[0:3]==b[0:3]):
   print("same")
else:
   print("not same")
   # write a program that reads two 3 digit numbers and check if the  first digit
   # of A is less than last digit of B
   A = input("enter the value of A")
   B = input("enter the value of B")
if (A[3]<B[-1]):
    print("first digit of a is less than last digit of b")
else:
    print("first digit of a is greater than last digit of b")


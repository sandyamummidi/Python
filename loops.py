#print solid square
#n=int(input("enter the digit"))
n=3
for i in range(1,n) :
    for j in range(1,n):
       print("*",end='')
    print( )
#sum of given numbers
a=[10,20,30,40,50]
sum=0
for i in list(a):
    sum +=i
print(sum)
#sum of natural numbers
n=int(input("enter the number"))
sum=0
for i in range(1,n):
    sum +=i
print(sum)
#product of given numbers
a=int(input("enter the num1"))
b=int(input("enter the num2"))
print(a*b)
#print solid rectangle
n=5
for i in range(1,n-2) :
    for j in range(1,n):
       print("*",end='')
    print( )
#or second model
n1=int(input("n1"))
n2=int(input("n2"))
for i in range(1,n):
    for j in range(1,n):
       print("*",end='')
    print( )



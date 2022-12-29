#write a programme hollow square
n=int(input("enter the num"))
for i in range(1,n+1):
    for j in range(1,n+1):
       if(i==1 or i==n or j==1 or j==n ):
           print("*",end='')
       else:
            print(" ",end='')
    print()
#write a program to print a solid diamond of 2N-1 rows using asterisk character(*)
n=5
for i in range(n):
    print(""(5-i-1)+""(i+1))
    for j in range(5-1,0,-1):
        print(""(5-j)+""(j))

#sdfghjkl

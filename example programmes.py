#write a program to print common elements in 3 sets
set_a=set(input("enter the elements"))
set_b=set(input("enter the elements"))
set_c=set(input("enter the elements"))
d=set_a&set_b&set_c
print(d)
#write a program to remove duplicate numbers in the list
list_1=[]
n=int(input("enter the n value"))
for i in range(0,n):
    c=int(input())
    list_1.append(c)
    print(list_1)
    set_a=set(list_1)
print(type(list_1))
print(list(set_a))
#write a program to check superset,subset,disjoint set
#superset
set_a=set(input("enter the a set"))
set_b=set(input("enter the b set"))
superset_c=set_a.issuperset(set_b)
print(superset_c)
#subset
set_a=set(input("enter the a set"))
set_b=set(input("enter the b set"))
subset_c=set_a.issubset(set_b)
print(subset_c)
#disjoint set
set_a = set(input("enter the a set"))
set_b = set(input("enter the b set"))
set_c = set_a.isdisjoint(set_b)
print(set_c)
#another method for removing duplicate numbers
list_a=list(map(int,input().split(' ')))
set_a=set(list_a)
list_b=list(set_a)
print(list_b)
# write a program to remove a list of numbers if present in the set...read inputs as comma separated
set_a=set(input("enter the set"))
print(type(set_a))
new_set= remove[2]
print(set_a)
#given two lines of comma-separated integers,write a program to print the numbers that are present in both the lines
list_a=list(map(int,input().split( )))
#first line contains comma separated integers.The second line of input will contain an integer(k)."5,3,7,9,5,6,2,1,8" k is 9
list_a=[5,3,7,9,5,6,2,1,8]
k=9
a=[]
for i in range(len(list_a)):
    for j in range (i+1,len(list_a)):
        if(list_a[i]+list_a[j]==k):
            list_b=(list_a[i],list_a[j])
            a.append(list_b)
print(a)
print(k)
#write a program the rotates list d times to the left
set_a=set(input("enter the values"))
print(type(set_a))
#write min and max program in python
set_a={1,2,3,4,5}
print(min(set_a))
print(max(set_a))
#character frequency.The input string will contain only alphabets and whitespaces.Ignore case sensitivity."Pop Up" o:1 p:3
# u:1,tic tac toe
#write a program the rotates list d times to the left
list_a=list(map(int,input().split('')))
n=int(input("value"))
for i in range(n):
    t=lis_a[0]
    list_a.remove(t)
    list_a.append(t)
       print(list_a)
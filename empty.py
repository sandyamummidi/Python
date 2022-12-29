l=list(map(int,input().split(' ')))
set_a=set(l)
list_b=list(set_a)
print(list_b)
#qqqwertyu
set_a={1,2,3}
value=1
print(type(value))
if value in set_a:
    print(set_a.remove(value))
else:
    print("doesnot remove")
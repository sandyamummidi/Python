# print addition of multiple numbers
# print remainder ,quotient of the  division ,print both integer and float results

list_a=[1,2,3,5]
list_b=list_a
print(id(list_a))
print(id(list_b))
list_b[0]=4
print(list_a)
print(list_b)
numbers="1 2 3 4"
num_list=numbers.split()
print(num_list);
numbers="1,2,34"
num_list=numbers.split( )
print(num_list)
list_x=["a","b","c","d"]

list_y = list_x[0:3]+list_x[5:8]
print(list_y)

print( list_y)




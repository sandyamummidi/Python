s=input("enter the string :")
count1=0
count2=0
for i in s:
    if i.isupper():
        count1+=1
    elif i.islower():
        count2+=1
print("lower:",count2)
print("upper is ",count1)

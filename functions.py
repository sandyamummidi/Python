#write function which accepts bill amount as arguments .if bill amount is less than 500,discount should be 5%.if bill amount is
#amount is greater than or equal to 500 and less than 2500 the discount is 10%,if the bill amount is greater than or equal
#to 2500 discount is 20%...print actual amount and discount amount.
bill =int(input("enter the bill amount"))
if bill<500:
    bill_1=bill*0.05
    actual_amount=bill-bill_1
    print('The discount amount is:', bill_1)
    print('The actual amount:',actual_amount)
elif bill>=500 and bill<=2500:
    bill_2=bill*0.1
    actual_amount = bill - bill_2
    print('The discount amount is:',bill_2)
    print('The actual amount:', actual_amount)
else:
    bill_3=bill*0.2
    actual_amount = bill - bill_3
    print('The discount amount is:',bill_3)
    print('The actual amount:', actual_amount)
#write a function that takes number of wins,draws and losses and calculate the number of points.each win is 4 points,
#draw is 2 points,loss is -1.input is single string containing win,draws an losses by comma seperated.The output is
#single line containing total points
w=int(input("enter the no.of wins"))
print(type(w))
d=int(input("enter the no.of draws"))
l=int(input("enter the no.of losses"))
print("Total no.of wins:",w*4)
print("Total no.of draws:",d*2)
print("Total no.of losses:",w-1)
print("Total no.of points:",)
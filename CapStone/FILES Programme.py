#files creation programme
for int in range(97,123):
    c=chr(int)
    with open(c+".txt",'w')as k:
        k.write(c)
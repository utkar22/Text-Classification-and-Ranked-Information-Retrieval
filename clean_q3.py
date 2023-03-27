f = open("q3.txt","r")
x = f.readlines()
f.close()

f2 = open("q3_clean.txt","w")
for i in x:
    l = i.split()
    if l[1] == "qid:4":
        print(i,end='',file=f2)
f2.close()
    

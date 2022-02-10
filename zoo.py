n = input("enter a word :- ")
zc=0
oc=0
for i in range(0,len(n)):
   
    if(n[i]=='z'):
        zc+=1
    else:
        oc+=1
        
if(2*zc==oc):
    print("yes")
else:
    print("no")

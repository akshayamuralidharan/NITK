import time

f=open("rosalind_ctbl.txt","r")
l=f.read()
print l
l=l[:-2]
f.close()

ch='('
f=open("output.txt","w")
t=time.time()

cb=[i for i, letter in enumerate(l) if letter == ')']
ob=[i for i, letter in enumerate(l) if letter == ch]

i=len(ob)-1


tp=l[0:]
tp=tp.replace('(','')
tp=tp.replace(')','')
tp=tp.split(',')
tp.sort()
print tp
#print ob,cb
while i>0:
        temp=filter(lambda x: x>ob[i],cb)
        temp=temp[0]
        tp2=l[ob[i]+1:temp]
        #print tp2
        tp2=tp2.replace('(','')
        tp2=tp2.replace(')','')
        tp2=tp2.split(',')
        ans=""
        #print ob[i],temp,tp2
        for ele in tp:
            if ele in tp2:
                ans=ans+'1'
            else:
                ans=ans+'0'
        #print ans
        f.write(ans+"\n")
        del ob[i]
        del cb[cb.index(temp)]
        i=i-1
        

#print l,ob,cb
		
t2=time.time()
f.close()

f=open("time.txt","w")
f.write("Exection Time: "+str(t2-t))
f.close()

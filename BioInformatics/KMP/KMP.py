import time

t = time.time()

f=open("rosalind_kmp.txt","r")

target=""
l=f.read().split('\n')
l=l[1:]
f.close()

for lin in l:
    target=target+lin

fail=[-1]  

j=-1

for k in range(len(target)):
    while j>=0 and target[k]!=target[j]:
        j=fail[j]
        
    j+=1        
    fail.append(j)

f=open("output_kmp.txt","wb")

t2 = time.time()

for i in fail[1:]:
    f.write(' '+str(i))
f.close()
for i in fail[1:]:
    print i, 


f=open("time.txt","w")
f.write("Execution Time: "+str(t2-t))
f.close()

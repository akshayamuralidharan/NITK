import sets
import time

ip=open("rosalind_seto.txt","r")
n=int(ip.readline())
y=ip.readline().strip().replace("}","").replace("{","").replace(",","").split()
z=ip.readline().strip().replace("}","").replace("{","").replace(",","").split()
a=[int(x) for x in y]
b=[int(x) for x in z] 
ip.close()
sa=sets.Set(a) 
sb=sets.Set(b)
k=[]
def set2list(sa):
    return [k for k in sa]   
tim = time.time()
k.append(set2list(sa.union(sb))) 
k.append(set2list(sa.intersection(sb))) 
k.append(set2list(sa.difference(sb))) 
k.append(set2list(sb.difference(sa))) 
def comp(n,s):
    k=[]
    for i in range(1,n+1):
        if i not in s:
            k.append(i)
    return k
k.append(comp(n,a))   
k.append(comp(n,b))
tim2 = time.time()
def prt(fp,k):
    fp.write("{")
    for i in range(len(k)):
        fp.write(str(k[i]))
        if not i:
            print "{"+str(k[i])+",",
        if not i== len(k)-1:
            fp.write(", ")
            if i:
                print str(k[i])+",",
        else:
            fp.write("}\n")
            print str(k[i])+"}"
    return   
op=open("output_seto.txt","w")
for i in k:
    prt(op,i)
op.close()


f=open("time.txt","w")
f.write("Execution Time: "+str(tim2-tim))
f.close()

import time

ip=open("rosalind_pdst.txt","r")
strs=[]
k=-1
for lin in ip:
    if lin.startswith(">"):
        k+=1
        strs.append("")
    else:
        strs[k]+=lin.strip()
ip.close()

def prop(s1,s2):
    cnt=0
    for i in range(len(s1)):
        if s1[i]!=s2[i]:
            cnt+=1
    return 1.0000*cnt/len(s1)
op=open("output_pdst.txt","w")
tim = time.time()
for i in strs:
    for j in strs:
        d=prop(i,j)  
        print d,
        op.write(str(d)+" ")
    print ""
    op.write("\n")
    


f=open("time.txt","w")
f.write("Execution Time: "+str(time.time()-tim))
f.close()

op.close()

import sys
import time
dep=sys.getrecursionlimit()   
tim = time.time()   
ip=open("rosalind_lcsq.txt","r")

st=[]
k=-1
for lin in ip:
    if lin.startswith(">"):
        st.append("")
        k+=1
    else:
        st[k]+=lin.strip()

ip.close()
lft=st[0]
top=st[1]
sys.setrecursionlimit(max(len(top),len(lft))+1500)
c=[]
k=0
for i in range(len(lft)+1):
    c.append([])
    for j in range(len(top)+1):
        c[k].append(0)     
    k+=1
for i in range(len(lft)):
    for j in range(len(top)):
        l=i+1
        t=j+1
        if lft[i]==top[j]:   
            c[l][t]=c[l-1][t-1]+1
        else:
            c[l][t]=max(c[l-1][t],c[l][t-1])
def back(c,lft,top,i,j):     
    if not ( i and j ):
        return ""
    elif lft[i-1]==top[j-1]:
        return back(c,lft,top,i-1,j-1)+lft[i-1]
    else:
        if c[i][j-1] > c[i-1][j]:
            return back(c,lft,top,i,j-1)
        else:
            return back(c,lft,top,i-1,j)
ans=back(c,lft,top,len(lft),len(top))  
tim2 = time.time()
op=open("output_lcsq.txt","w")
op.write(ans)
print ans
op.close()
sys.setrecursionlimit(dep)


f=open("time.txt","w")
f.write("Execution Time: "+str(tim2-tim))
f.close()

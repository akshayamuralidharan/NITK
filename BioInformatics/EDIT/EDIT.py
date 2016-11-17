import time


tim=time.time()
ip=open("rosalind_edit.txt","r")
k=-1
st=[]
for lin in ip:
    if lin.startswith(">"):
        k+=1
        st.append("")
    else:
        st[k]+=lin.strip()
ip.close()
lft=st[0]
top=st[1]
mat=[]
for i in range(len(lft)+1):
    mat.append([i])
for j in range(len(top)):
    mat[0].append(j+1)
for i in range(len(lft)):
    for j in range(len(top)):
        l=i+1
        t=j+1
        flg=1
        if lft[i]==top[j]:
            flg=0
        mat[l].append(min(mat[l-1][t]+1,mat[l][t-1]+1,mat[l-1][t-1]+flg))
op=open("output_edit.txt","w")
ans=mat[len(lft)][len(top)]
op.write(str(ans))
op.close()
print ans


f=open("time.txt","w")
f.write("Execution Time: "+str(time.time()-tim))
f.close()

import sys
import time


ip=open("rosalind_scsp.txt","r")
dna1=ip.readline().strip()
dna2=ip.readline().strip()
ip.close()
lft=dna1
top=dna2
sys.setrecursionlimit(max(len(top),len(lft))+1500)  
c=[]
k=0
tim=time.time()
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
lcsq=back(c,lft,top,len(lft),len(top))


superseq = ['']*(len(lcsq)+1) 
d1i = d2i = 0

for i in range(len(lcsq)+1):
	if i == len(lcsq):
		superseq[len(lcsq)] = dna1[d1i:]+dna2[d2i:]
		superseq = ''.join(superseq)
	else:
		while dna1[d1i] != lcsq[i] and d1i < len(dna1):
			superseq[i] += dna1[d1i]
			d1i += 1
		while dna2[d2i] != lcsq[i] and d2i < len(dna2):
			superseq[i] += dna2[d2i]
			d2i += 1
		superseq[i] += lcsq[i]
		d1i += 1
		d2i += 1

tim2=time.time()

f=open("time.txt","w")
f.write("Execution Time: "+str(tim2-tim))
f.close()

op=open("output_scsp.txt","w")
op.write(str(superseq))
op.close()

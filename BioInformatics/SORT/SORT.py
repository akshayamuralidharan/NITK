import time
from itertools import product,compress

def bpfind(x,y):
    return abs(x-y)!=1
def reversal(perm,start,stop):
    return perm[:start]+perm[start:stop+1][::-1]+perm[stop+1:]
def bpc(permutation): 
    permutation = [0] + list(permutation) + [len(permutation)+1] 
    return sum(map(bpfind, permutation[1:], permutation[:-1]))
def bpi(permutation): 
    permutation = [0] + list(permutation) + [len(permutation)+1]
    return compress(range(len(permutation)-1), map(bpfind, permutation[1:], permutation[:-1]))
    

def bfs_min(perm1, perm2):
    linear = {value: i + 1 for i, value in enumerate(perm2)} # 
    indices = [linear[value] for value in perm1]
    indices = tuple(indices)
    current_perms = {indices:[]}
    min_breaks = bpc(indices)
    dist = 0


    while True:
        new_perms = {}
        dist+=1
    
        for perm in current_perms.keys():
            for ri in product(bpi(perm), repeat=2):  
                
                start = ri[0]
                stop = ri[1]-1
                temp_perm = tuple(reversal(perm, start,stop))
                temp_breaks = bpc(temp_perm)
                temp_transformation = current_perms[perm] + [str(start+1) + ' ' + str(stop)]
                
                if temp_breaks == 0:
                    return temp_transformation 

                
                elif temp_breaks < min_breaks:
                    min_breaks = temp_breaks
                    new_perms = {temp_perm:temp_transformation}

                
                elif temp_breaks == min_breaks:
                    new_perms[temp_perm]=temp_transformation

        current_perms = new_perms
k=0
source=[] 
destination=[] 

ip=open("rosalind_sort.txt","r")
src=ip.readline().strip().split()
destn=ip.readline().strip().split()
ip.close()
op=open("output_sort.txt","w")
tim=time.time()
ans=bfs_min(src,destn)
ans=[str(len(ans))]+ans
for i in range(1,len(ans)):
    m=ans[i].split()
    m[0]=int(m[0])
    m[1]=int(m[1])+1
    ans[i]=' '.join(map(str,m))
op.write('\n'.join(ans))


f=open("time.txt","w")
f.write("Execution Time: "+str(time.time()-tim))
f.close()



op.close()




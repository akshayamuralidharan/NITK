import time
from itertools import product,compress

def bpfind(x,y):
    return abs(x-y)!=1
def reversal(perm,start,stop):
    return perm[:start]+perm[start:stop+1][::-1]+perm[stop+1:]
def bpc(permutation): #counting breakpoints
    permutation = [0] + list(permutation) + [len(permutation)+1] 
    return sum(map(bpfind, permutation[1:], permutation[:-1]))
def bpi(permutation): # counting number of breakpoints
    permutation = [0] + list(permutation) + [len(permutation)+1]
    return compress(range(len(permutation)-1), map(bpfind, permutation[1:], permutation[:-1]))
    

def bfs_min(perm1, perm2):
    linear = {value: i + 1 for i, value in enumerate(perm2)} # 
    indices = [linear[value] for value in perm1]
    indices = tuple(indices)
    current_perms = [indices]
    min_breaks = bpc(indices)
    dist = 0

    while True:
        new_perms = []
        dist+=1
        for perm in current_perms:
            for ri in product(bpi(perm), repeat=2): # start adn end 
                start = ri[0]
                stop = ri[1]-1
                temp_perm = tuple(reversal(perm, start,stop))
                temp_breaks = bpc(temp_perm)

                if temp_breaks == 0:
                    return dist

                elif temp_breaks < min_breaks:
                    min_breaks = temp_breaks
                    new_perms = [temp_perm]

                elif temp_breaks == min_breaks:
                    new_perms.append(temp_perm)

        current_perms = new_perms
k=0
source=[] 
destination=[] 

ip=open("rosalind_rear.txt","r")

for line in ip:
    if line.startswith('\n'):
        k=0
        continue
    vect=[int(i) for i in line.strip().split()]
    if not k:
        source.append(vect)
        k=1
    else:
        destination.append(vect) 
ip.close()

op=open("output_rear.txt","w")
tim=time.time()
for i in range(len(source)):
    src=source[i]
    destn=destination[i]
    ans=min(bfs_min(src,destn),bfs_min(destn,src))
    print ans,
    op.write(str(ans)+" ")
op.close()


f=open("time.txt","w")
f.write("Execution Time: "+str(time.time()-tim))
f.close()

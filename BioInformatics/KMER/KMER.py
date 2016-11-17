import itertools
import re
import time

f=open("rosalind_kmer.txt","r+")
l=f.read().split('\n')
l=l[1:]
f.close()

s=""

for ele in l:
    s=s+ele

ln=[]
l=['A','C','G','T']

tim=time.time()

l=list(itertools.product(l, repeat=4))

for i in range(256):
    sub=""
    sub="(?="+sub.join(l[i])+")"
    #print sub

    k=[m.start() for m in re.finditer(sub, s)]
    ln.append(len(k))

f=open("out.txt","w")
f.write(" ".join(str(e) for e in ln))
f.close()


f=open("time.txt","w")
f.write("Execution Time: "+str(time.time()-tim))
f.close()

import sys
import time

with open("rosalind_mmch.txt","r") as fp:
        rna=""
        for lines in fp:
                if not lines.startswith('>'):
                        rna+=lines.strip()
fp.close()


a = "AUGAUGAUCGCCCAUGAGAUGUGCCGGCUCUAAUUACCUGCGAGAGACUCGCCGCAGACGAACUUGCUUCGCGCAGACGAUGCGCUCU"
a=rna
A = 0
U = 0
G = 0
C = 0

def fac(n):
    if n is 0:
        return 1
    if n is 1:
        return 1
    else:
        return n*fac(n-1)

def min(a, b):
    if a < b:
        return a
    else:
        return b
def max(a, b):
    if a > b:
        return a
    else:
        return b

def comb(a, b):
    return fac(a)/fac(a-b)

for i in a:
    if i is "A":
        A += 1
    if i is "U":
        U += 1
    if i is "G":
        G += 1
    if i is "C":
        C += 1
        
tim = time.time()
print comb(max(A,U),min(A,U))*comb(max(G,C),min(G,C))
tim2 = time.time()


f=open("time.txt","w")
f.write("Execution Time: "+str(tim2-tim))
f.close()

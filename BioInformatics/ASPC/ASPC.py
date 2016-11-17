import time

ip=open("rosalind_aspc.txt","r")
n,m = map(int,ip.readline().strip().split())
ip.close()
fact=[1]

tim=time.time()

for i in range(1,n+1): 
    fact.append(fact[i-1]*i)
 
def comb(n,k):
    return fact[n]/(fact[k]*fact[n-k])

ans=sum([comb(n,k) for k in range(m,n+1)])%1000000  
op=open("output_aspc.txt","w")
op.write(str(ans))
op.close()


f=open("time.txt","w")
f.write("Execution Time: "+str(time.time()-tim))
f.close()

import time

tim = time.time()
ip=open("rosalind_sset.txt","r")
n=int(ip.readline()) 
op=open("output_sset.txt","w")

k=(2**n)%1000000

op.write(str(k))
tim2 = time.time()


f=open("time.txt","w")
f.write("Execution Time: "+str(tim2-tim))
f.close()


op.close()
ip.close()

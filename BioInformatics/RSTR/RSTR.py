import time

ip=open("rosalind_rstr.txt","r")
into=ip.readlines()
n,gc = int(into[0].split()[0]),float(into[0].split()[1])

tar=into[1].strip()
ip.close()
tim = time.time()
g=tar.count('G')+tar.count('C')  
a=tar.count('A')+tar.count('T')  
p=((gc/2.0)**g)*(((1-gc)/2.0)**a) 

c=(1-p)**n  
op=open("output_rstr.txt","w")
op.write(str(1-c)) 
op.close()
print 1-c


f=open("time.txt","w")
f.write("Execution Time: "+str(time.time()-tim))
f.close()

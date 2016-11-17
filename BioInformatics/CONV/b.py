import time

f=open("rosalind_conv.txt","r")
l=f.read().split('\n')
f.close()

s1=map(lambda x:float(x),l[0].split())
s2=map(lambda x:float(x),l[1].split())
s=[]


f=open("output.txt","w")
t=time.time()

for e1 in s1:
	for e2 in s2:
		s.append(round(e1-e2,5))
	
f.write(str(s.count(max(set(s), key=s.count)))+"\n")
f.write(str(max(set(s), key=s.count))+"\n")
		
t2=time.time()
f.close()

f=open("time.txt","w")
f.write("Exection Time: "+str(t2-t))
f.close()

import time

def revc(a):
	
	a=a.replace('A','a')
	a=a.replace('C','c')
	a=a.replace('G','C')
	a=a.replace('T','A')
	a=a.replace('c','G')
	a=a.replace('a','T')
	a=a[::-1]
	return a


f=open("rosalind_dbru_1_dataset.txt","r")
l=f.read().split('\n')
f.close()
s=[]

f=open("output.txt","w")
t=time.time()


for a in l:
	
	if revc(a) not in l and revc(a) not in s:
		s.append(revc(a))

for ele in l:
	if ele not in s:
		s.append(ele)
	

for ele in s:
	print "("+ele[:-1]+", "+ele[1:]+")"
	f.write("("+ele[:-1]+", "+ele[1:]+")"+"\n")

#f.write(str(max(set(s), key=s.count))+"\n")
		
t2=time.time()
f.close()

f=open("time.txt","w")
f.write("Exection Time: "+str(t2-t))
f.close()
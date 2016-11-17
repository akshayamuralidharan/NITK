import time

f=open("rosalind_trie.txt","r")
l=f.read().split('\n')
f.close()

d={1:[[],[]]}
n=2

f=open("output.txt","w")
t=time.time()


for wrd in l:
	p=1
	i=0
	flag=1
	
	while i < len(wrd) and flag:
		k=d[p]
		#print wrd[i]
		if wrd[i] in k[0]:
			p=k[1][k[0].index(wrd[i])]
			i=i+1
		else:
			flag=0
		
				
	while i < len(wrd):
		d[p][0].append(wrd[i])
		d[p][1].append(n)
		d[n]=[[],[]]
		f.write(str(p)+" "+str(n)+" "+wrd[i]+"\n")
		
		p=n
		n=n+1
		i=i+1
		
t2=time.time()
f.close()

f=open("time.txt","w")
f.write("Exection Time: "+str(t2-t))
f.close()
import time

already_fnd = {}
def givecomp(nuc):
    k='ACUG'
    return k[(k.index(nuc)+2)%4]  
def motz(rna):
	if len(rna)<=1:
		return 1  
	else:
		if rna in already_fnd:   
			return already_fnd[rna]
		else:
			si = []
			for i in range(1, len(rna)):
				if rna[0]==givecomp(rna[i]):
					si.append([rna[1:i],rna[i+1:]])  
			
			already_fnd[rna]=(sum([motz(subint[0])*motz(subint[1]) for subint in si]) + motz(rna[1:])
                                          ) % 1000000

			return already_fnd[rna]
with open("rosalind_motz.txt","r") as fp:
        m=""
        for lines in fp:
                if not lines.startswith('>'):
                        m+=lines.strip()
fp.close()
tim = time.time()
i=motz(m)
with open("output_motz.txt","w") as op:
        op.write(str(i))
        print i
        op.close()

        

f=open("time.txt","w")
f.write("Execution Time: "+str(time.time()-tim))
f.close()

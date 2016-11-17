import time
from numpy import zeros

def is_interwoven(dna1, dna2, superstr):
    
    
    if len(superstr) == 0:
        return True
    elif dna1[0] == dna2[0] == superstr[0]:
        return is_interwoven(dna1[1:], dna2, superstr[1:]) or is_interwoven(dna1, dna2[1:], superstr[1:])
    elif dna1[0] == superstr[0]:
        return is_interwoven(dna1[1:], dna2, superstr[1:])
    elif dna2[0] == superstr[0]:
        return is_interwoven(dna1, dna2[1:], superstr[1:])
    else:
        return False

if __name__ == '__main__':
    with open('rosalind_itwv_2_dataset.txt') as input_data:
        superstr = input_data.readline()
        dna = [line.strip() for line in input_data.readlines()]

    
    M = zeros((len(dna), len(dna)), dtype=int)
    t1=time.time()
    
    for i in xrange(len(dna)):
        for j in xrange(len(dna)):
            if i <= j:
                current_profile = [(dna[i]+dna[j]).count(nucleotide) for nucleotide in 'ACGT']
                for index in xrange(len(superstr)-len(dna[i])-len(dna[j])+1):
                    if current_profile == [superstr[index:index+len(dna[i])+len(dna[j])].count(nucleotide) for nucleotide in 'ACGT']:
                        if is_interwoven(dna[i]+'$', dna[j]+'$', superstr[index:index+len(dna[i])+len(dna[j])]):
                            M[i][j] = 1
                            break
            else:
                M[i][j] = M[j][i]
                
    t2=time.time()
    print '\n'.join([' '.join(map(str, M[i])) for i in xrange(len(dna))])
    #print "Sf"


  
f=open("time.txt","w")
f.write("Exection Time: "+str(t2-t1))
f.close()

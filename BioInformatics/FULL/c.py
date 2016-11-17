import time

WEIGHT_TABLE = {71.03711: 'A', 103.00919: 'C', 115.02694: 'D', 129.04259: 'E',
147.06841: 'F', 57.02146: 'G', 137.05891: 'H', 113.08406: 'I', 128.09496: 'K',
113.08406: 'L', 131.04049: 'M', 114.04293: 'N', 97.05276: 'P', 128.05858: 'Q',
156.10111: 'R', 87.03203: 'S', 101.04768: 'T', 99.06841: 'V', 186.07931: 'W',
163.06333: 'Y'}

def ful(parent, ions):

    pairs = []
    index = 0
    sequence = ''
    
    while index < len(ions) / 2:
        closest_partner = 0
        distance = 400
        
        for ion in ions:
            if abs(parent - ions[index] - ion) < distance:
                closest_partner = ion
                distance = abs(parent - ions[index] - ion)
        
        pairs.append((ions[index], closest_partner))
        index += 1
    
    index = 0
    print "done"
    pairs.sort()
    
    while index < len(ions)/2-1:
        nearest_candidate = None
        print index

        for candidate in WEIGHT_TABLE.keys():
                
            if round(abs(pairs[index + 1][0] - pairs[index][0] - candidate), 3) == 0:
                nearest_candidate = candidate
        
        if not nearest_candidate:
            pairs[index + 1] = (pairs[index + 1][1], pairs[index + 1][0])
            pairs.sort()
            
            index = 0
            sequence = ''
        else:
            sequence = ''.join([sequence, WEIGHT_TABLE[nearest_candidate]])
            index += 1

    return sequence




f= open('rosalind_full.txt')
parent_weight = float(f.readline().strip())
l=[]
    
for line in f:
        l.append(float(line.strip()))


f.close()



f=open("output.txt","w")
t=time.time()

ans=ful(parent_weight, l)


f.write(ans+"\n")


		
t2=time.time()
f.close()

f=open("time.txt","w")
f.write("Exection Time: "+str(t2-t))
f.close()

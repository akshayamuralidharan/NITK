import time

tim=time.time()
class Node:
    def __init__(self, lab):
        self.f = self.t = 0
        self.s = set()
        self.lab = lab
    def __repr__(self):
        return tuple(map(str, (self.lab, self.f, self.t, self.s)))
def get_longest_substring(r, l):
    global longestl, lstring
    substring = 0
    if r.t == len(dnas):
        return 1  
    str_collection.append((r.f, r.t))
    for son in r.s:
        substring += get_longest_substring(son, l + r.t - r.f)
    if substring >= k and l + r.t - r.f > longestl:
        lstring = list(str_collection)
        longestl = l + r.t - r.f
    str_collection.pop()
    return substring
child = set()
nodes = {}
longestl = 0
lstring = []
str_collection = []
ip=open('rosalind_lrep_1_dataset.txt','r')
dnas = ip.readline().strip()
k = int(ip.readline().strip())        
for x in map(str.strip, ip.readlines()):
    a, b, loc, tl = x.split()        
    na = nodes.setdefault(a, Node(a))
    nb = nodes.setdefault(b, Node(b))
    nb.f = int(loc) - 1
    nb.t = int(loc) + int(tl) - 1        
    na.s.add(nb)
    child.add(nb)            
ip.close()
root = (set(nodes.values()) - child).pop()        
get_longest_substring(root, 0)    
final=''.join(dnas[i:j] for (i, j) in lstring)
op=open("output_lrep.txt","w")
op.write(final)
op.close()


  

f=open("time.txt","w")
f.write("Exection Time: "+str(time.time()-tim))
f.close()

    



    
    
    

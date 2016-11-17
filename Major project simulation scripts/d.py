import time
import networkx as nx

f=open("sample1.txt")

g=[]


G=nx.barabasi_albert_graph(20000,10)
  
g=[[0 for j in range(20000)] for k in range(20000)]

for (u,v) in G.edges():
    g[u][v]=1
n=len(g)
for i in range(n):
    for j in range(n):
        g[j][i]=g[i][j]

f=open("Contaminated.txt")

S=map(lambda a:int(a),f.readline().strip().split(' '))

f=open("Weights.txt")

W=map(lambda a:int(a),f.readline().strip().split(' '))

f=open("MaxCost.txt")

maxcost=int(f.readline().strip())
d={}

for i in range(n):
    for j in range(n):
        if g[i][j]>0:
            if i not in d:
                d[i]=1
            else:
                d[i]=d[i]+1
    
L=[]
Ladj={}
curr_cost=0
v_cost=0
start = time.clock()

for v in S:
    for i in range(n):
        if i not in S and g[v][i]!=0:
           # L.append((v,i,g[v][i]))
            if i not in Ladj:
                Ladj[i]=1
            else:
                Ladj[i]=Ladj[i]+1
            #curr_cost=curr_cost+g[v][i]
   # v_cost=v_cost+W[v]

while len(Ladj)>0:
    #print d
    #print Ladj
    max_value = max(2*Ladj[i] - d[i] for i in Ladj)
    #print max_value
    temp = [i for i in Ladj if 2*Ladj[i]-d[i] == max_value]
    #print temp
    del Ladj[temp[0]]
    
            
    if max_value>-6:
        for i in Ladj:
        #for j in range(n):
            if g[i][temp[0]]>0:
                Ladj[i]=Ladj[i]+1

        S.append(temp[0])
        for i in range(n):
            if i not in S and g[temp[0]][i]>0:
                if i not in Ladj:
                    Ladj[i]=1
    

"""
while len(L)>0 and curr_cost+v_cost>maxcost:
    max_value = max(ele[2] for ele in L)
    temp= [x for x in L if x[2] == max_value]
    (u,v,w)=temp[0]
    L.remove(temp[0])
    curr_cost=curr_cost-w
    
    if v not in S and W[v]<w:
        S.append(v)
        v_cost=v_cost+W[v]

        for edge in L:
            if edge[0]==v or edge[1]==v:
                L.remove(edge)
                curr_cost=curr_cost-edge[2]
        for i in range(n):
            if i not in S:
                if g[v][i]>0:
                    L.append((v,i,g[v][i]))
                    curr_cost=curr_cost+g[v][i]

end = time.clock()

print "Cost: ",curr_cost+v_cost
print S
if (curr_cost>maxcost):
    print "No solution found within cost."

print "Time taken: ", end - start
"""
print S
nok=0
for i in S:
    for j in range(n):
        if j not in S and g[i][j]>0:
           # print i,j
            nok=nok+1
print "Number of Edges:",nok
print "Number of Nodes:",len(S)

f=open('ansr0000.txt','r')

ans=f.read().strip().split(' ')

f.close()
f=open('ansr0000.txt','w')

ans[0]=int(ans[0])+nok
ans[1]=int(ans[1])+len(S)
ans[2]=int(ans[2])+1
f.write(str(ans[0])+' ')
f.write(str(ans[1])+' ')
f.write(str(ans[2]))
f.close()

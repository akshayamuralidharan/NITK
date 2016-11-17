import time
#import networks as nw

f=open("Graph.txt")

g=[]

for line in f:
    g.append(map(lambda a: int(a),line.strip().split(' ')))

#fast_gnp_random_graph(5,g)
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


L=[]
curr_cost=0
v_cost=0
start = time.clock()
for v in S:
    for i in range(n):
        if i not in S and g[v][i]!=0:
            L.append((v,i,g[v][i]))
            curr_cost=curr_cost+g[v][i]
    v_cost=v_cost+W[v]

mincost=curr_cost+v_cost
MinS=map(lambda x:x,S)

while len(L)>0:
    max_value = max(ele[2] for ele in L)
    temp = [x for x in L if x[2] == max_value]
    (u,v,w)=temp[0]
    L.remove(temp[0])
    #curr_cost=curr_cost-w
    wt=0
    gwt=0
    for ele in S:
        wt=wt+g[ele][v]
    if v not in S and W[v]<wt:
        S.append(v)
        v_cost=v_cost+W[v]
        curr_cost=curr_cost-w
        for edge in L:
            if edge[0]==v or edge[1]==v:
                L.remove(edge)
                curr_cost=curr_cost-edge[2]
        for i in range(n):
            if i not in S:
                if g[v][i]>0:
                    L.append((v,i,g[v][i]))
                    curr_cost=curr_cost+g[v][i]
    if mincost>curr_cost+v_cost:
        mincost=curr_cost+v_cost
        MinS=map(lambda x:x,S)

end = time.clock()

print "Cost: ",curr_cost+v_cost
print S
print "MinCost: ",mincost
print MinS

if (curr_cost>maxcost):
    print "No solution found within cost."

print "Time taken: ", end - start

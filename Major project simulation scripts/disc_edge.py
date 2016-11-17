import networkx as nx
from asp import all_shortest_paths
import operator



#G=nx.barabasi_albert_graph(10,3)
  
#S=[2,3,5]
def disc_edge(H,k):
    G=H.copy()
    for i in range(k):
        a=edge_centrality(G)
        if a[0]==-1:
            return G
        G.remove_edge(a[0],a[1])
    return G



def edge_centrality(G):
    

    paths=[]



    for s in G.nodes():
        for d in G.nodes():
            #print [p for p in all_shortest_paths(G,source=s,target=d)]
            #print
            try:
                temp=all_shortest_paths(G,source=s,target=d)
                paths=paths+[p for p in temp]
  
            except Exception:
                #print paths
                pass
            

    mis={}

    for l in paths:
        for i in range(len(l)-1):
            if l[i]>l[i+1]:
                a=l[i+1]
                b=l[i]
            else:
                a=l[i]
                b=l[i+1]
            
            if (a,b) not in mis:
                mis[(a,b)]=1
            else:
                mis[(a,b)]=mis[(a,b)]+1

    #print mis
    if len(mis)>0:            
        ind=max(mis.iteritems(), key=operator.itemgetter(1))[0]
    else:
        return (-1,-1)
    #print ind
    return ind
    

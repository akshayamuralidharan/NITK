import networkx as nx
from asp import all_shortest_paths
from spl import shortest_path_length
import operator


#G=nx.barabasi_albert_graph(10,3)
  
#S=[2,3,5]


def inf_centrality_s(G, S):
    

    paths=[]
    spl={}
    for s in S:
        for d in G.nodes():
            if d not in S:
                paths=paths+[p for p in all_shortest_paths(G,source=s,target=d)]

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
    return mis

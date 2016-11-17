from priodict import priorityDictionary
def centrality(G,S):
    don=[]
    centp={}
    centn={}
    
    for v in G:
        centp[v]=0
        centn[v]=0
    for v in G:
        dis,pred=Dijkstra(G,v)
        for u in G:
            inf=0
            if(u,v) and (v,u) not in don:
                for node in pred:
                    node1=node
                    while node1!=v:
                        if pred[node1] in S:
                            inf=1
                            break
                        node1=pred[node1]
                        
                    node1=node    
                    while node1!=v:
                        if inf==1:
                            centn[pred[node1]]=centn[pred[node1]]+1
                        else:
                            centp[pred[node1]]=centp[pred[node1]]+1
                        
                        node1=pred[node1]
            don.append((v,u))
    print centp
    print centn
                    
                    
        
    
    
def Dijkstra(G,start,end=None):
	
    D = {}	# dictionary of final distances
    P = {}	# dictionary of predecessors
    Q = priorityDictionary()   # est.dist. of non-final vert.
    Q[start] = 0
    for v in Q:
        D[v] = Q[v]
        
        if v == end:
            break
        for w in G[v]:
            vwLength = D[v] + G[v][w]
            if w in D:
                if vwLength < D[w]:
                    raise ValueError, \
  "Dijkstra: found better path to already-final vertex"
            elif w not in Q or vwLength < Q[w]:
                Q[w] = vwLength
                P[w] = v
	
    return (D,P)


di={0:{1:1,2:1,4:1},1:{0:1,3:1},2:{0:1,4:1},3:{1:1},4:{0:1,2:1}}

print Dijkstra(di, 2)
centrality(di,[2,3])

import operator

def remove_edges(H, edgelist, k):
        G=H.copy()
	#print edgelist
	#print G.edges()
	sorted_edges = sorted(edgelist.items(), key=operator.itemgetter(1))
	sorted_edges.reverse()
	#print sorted_edges
	for i in range(k):
		
		try:
                        G.remove_edge(sorted_edges[i][0][0],sorted_edges[i][0][1])
               
                except Exception:
                #print paths
                        pass


	return G


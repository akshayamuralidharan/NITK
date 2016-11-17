import networkx as nx
import random
from centrality2 import edge_centrality
from centrality_s import inf_centrality_s
from centrality import inf_centrality
from disc_edge import disc_edge
from remove_edges import remove_edges



        #n=200                                                     #number of nodes in graph
        #d=7
        #m=5                                                     #contaminated seed set size
        #p=0.05                                                   #propagation probability
        #k=50                                                    #number of edges to be removed


def main1(n,d,m,p,k):

        G=nx.barabasi_albert_graph(n,d)        
        print 
        S =[]
        
        US =[]
        US1=[]
        US2=[]
        US3=[]
        US4=[]
       

        for i in range(m):
                rval=random.randrange(n)
                S.append(rval)
                US.append(rval)
                US1.append(rval)
                US2.append(rval)
                US3.append(rval)
                US4.append(rval)

                
        #print S
        #print G.edges()
        ic=inf_centrality(G,S)
        ics=inf_centrality_s(G,S)
        ec=edge_centrality(G)
        G4=disc_edge(G,k)
        G3=remove_edges(G,ic,k)
        G2=remove_edges(G,ics,k)
        G1=remove_edges(G,ec,k)

        #print G1.edges()
        #print G2.edges()

        ni0=len(S)
        ni1=len(S)
        ni2=len(S)
        ni3=len(S)
        ni4=len(S)

        for i in range(7):
                print i
                
                P=[]
                for u in S:
                        N=G.neighbors(u)
                        
                        for v in N:
                                rval=random.randrange(100)
                                if p*100 > rval and v not in US:
                                        print "Adding",v,"to S"
                                        P=P+[v]
                                        US=US+[v]
                                        ni0=ni0+1
                                        if (u,v) in G1.edges() or (v,u) in G1.edges():
                                                print "Adding",v,"to S1"
                                                ni1=ni1+1
                                                US1.append(v)
                                        if (u,v) in G2.edges() or (v,u) in G2.edges():
                                                print "Adding",v,"to S2"
                                                ni2=ni2+1
                                                US2.append(v)
                                        if (u,v) in G3.edges() or (v,u) in G3.edges():
                                                print "Adding",v,"to S3"
                                                ni3=ni3+1
                                                US3.append(v)
                                        if (u,v) in G4.edges() or (v,u) in G4.edges():
                                                print "Adding",v,"to S4"
                                                ni4=ni4+1
                                                US4.append(v)
                                       
                                        
                S=[]
                for u in P:
                        S.append(u)

               


                
        return [ni0,ni1,ni2,ni3,ni4]


print main1(100,5,5,0.05,50)

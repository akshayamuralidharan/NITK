import networkx as nx

def shortest_path_length(G, source=None, target=None, weight=None):
    """Compute shortest path lengths in the graph.

    This function can compute the single source shortest path
    lengths by specifying only the source or all pairs shortest
    path lengths by specifying neither the source or target.

    Parameters
    ----------
    G : NetworkX graph

    source : node, optional
       Starting node for path.
       If not specified compute shortest path lengths for all
       connected node pairs.

    target : node, optional
       Ending node for path.
       If not specified compute shortest path lengths for every
       node reachable from the source.

    weight : None or string, optional (default = None)
       If None, every edge has weight/distance/cost 1.
       If a string, use this edge attribute as the edge weight.
       Any edge attribute not present defaults to 1.

    Returns
    -------
    length : number, or container of numbers
        If the source and target are both specified return a
        single number for the shortest path.
        If only the source is specified return a dictionary keyed by
        targets with a the shortest path as keys.
        If neither the source or target is specified return a dictionary
        of dictionaries with length[source][target]=value.

    Raises
    ------
    NetworkXNoPath
        If no path exists between source and target.

    Examples
    --------
    >>> G=nx.path_graph(5)
    >>> print(nx.shortest_path_length(G,source=0,target=4))
    4
    >>> p=nx.shortest_path_length(G,source=0) # target not specified
    >>> p[4]
    4
    >>> p=nx.shortest_path_length(G) # source,target not specified
    >>> p[0][4]
    4

    Notes
    -----
    For digraphs this returns the shortest directed path.
    To find path lengths in the reverse direction use G.reverse(copy=False)
    first to flip the edge orientation.

    See Also
    --------
    all_pairs_shortest_path_length()
    all_pairs_dijkstra_path_length()
    single_source_shortest_path_length()
    single_source_dijkstra_path_length()

    """
    if source is None:
        if target is None:
            if weight is None:
                paths=nx.all_pairs_shortest_path_length(G)
            else:
                paths=nx.all_pairs_dijkstra_path_length(G, weight=weight)
        else:
            raise nx.NetworkXError("Target given but no source specified.")
    else: # source specified
        if target is None:
            if weight is None:
                paths=nx.single_source_shortest_path_length(G,source)
            else:
                paths=nx.single_source_dijkstra_path_length(G,source,weight=weight)
        else:
            # shortest source-target path
            if weight is None:
                p=nx.bidirectional_shortest_path(G,source,target)
                paths=len(p)-1
            else:
                paths=nx.dijkstra_path_length(G,source,target,weight)
    return paths

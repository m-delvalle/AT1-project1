"""
Algorithmic Thinking - Part 1
Project 1 - Graph basics
CodeSkulptor ID: user40_ILWP9XVessBDVGu
"""

__author__ = 'manuel'


# Graph examples (global constants)
EX_GRAPH0 = {0: set([1, 2]), 1: set([]), 2: set([])}

EX_GRAPH1 = {0: set([1, 4, 5]), 1: set([2, 6]), 2: set([3]), 3: set([0]),
             4: set([1]), 5: set([2]), 6: set([])}

EX_GRAPH2 = {0: set([1, 4, 5]), 1: set([2, 6]), 2: set([3, 7]), 3: set([7]),
             4: set([1]), 5: set([2]), 6: set([]), 7: set([3]), 8: set([1, 2]),
             9: set([0, 3, 4, 5, 6, 7])}


def make_complete_graph(num_nodes):
    """
    Creates a "complete" directed graph ("digraph") of 'num_nodes' nodes.
    A complete digraph contains all possible edges subject to the restriction
    that self-loops are not allowed.
    The nodes of the digraph should be numbered 0 to num_nodes - 1
    when num_nodes is positive. Otherwise, the function returns a dictionary
    corresponding to the empty digraph.

    :param num_nodes: the number of nodes the new digraph will contain
    :type num_nodes: int

    :return: a complete digraph of 'num_nodes' nodes.
    :rtype: dict
    """
    digraph = {}
    for node_id in xrange(num_nodes):
        digraph[node_id] = set([])
        for to_node in xrange(num_nodes):
            if to_node != node_id:
                digraph[node_id].add(to_node)
    return digraph


def in_degree(graph, node):
    """
    Computes the in-degree (in case of a digraph) or the degree (in case of
    an undirected graph) of the given node.

    :param graph: The given graph/digraph, represented as a dict {node: set(incident_to)}
    :type graph: dict
    :param node: the given node.
    :type node: object

    :return: The degree/in-degree of node.
    :rtype: int
    """
    count = 0

    for n in graph:
        for to_node in graph[n]:
            if to_node == node:
                count += 1

    return count


def compute_in_degrees(digraph):
    """
    Computes the in-degree of all nodes in directed graph 'digraph'.
    Returns a dictionary with the same set of keys (nodes) as 'digraph'
    and whose corresponding values are the number of edges whose head
    matches a particular node.

    :param digraph: The given digraph, represented as a dict {node: set(incident_to)}
    :type digraph: dict

    :return: a dictionary associating each node_id with it's degree
    :rtype: dict
    """
    in_degrees = {}
    for node in digraph:
        in_degrees[node] = in_degree(digraph, node)
    return in_degrees


def make_dict(keys, default_value=0):
    """
    Creates a new dictionary with the specified keys and default value.

    :param keys: A list of keys to be included in the returned dictionary.
    :type keys: list
    :param default_value: The initial mapping value for each key.
    :type default_value: object

    :return: A dictionary where every key is mapped to the given default_value.
    :rtype: dict
    """
    result = {}

    for key in keys:
        result[key] = default_value

    return result


def in_degree_distribution(digraph):
    """
    Computes in-degrees unnormalized distribution as a dict whose keys
    correspond to in-degrees of nodes in the graph. The value associated
    with each particular in-degree is the number of nodes with that in-degree.
    In-degrees with no corresponding nodes in the graph are not included.

    :param digraph: The given digraph, represented as a dict {node: set(incident_to)}
    :type digraph: dict

    :return: a dictionary associating each value of in-degree with the amount
             of nodes with that in-degree
    :rtype: dict
    """
    in_degrees = compute_in_degrees(digraph)
    in_deg_dist = make_dict(in_degrees.keys())
    for in_deg in in_degrees.itervalues():
        in_deg_dist[in_deg] += 1
    return in_deg_dist

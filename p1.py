"""
Algorithmic Thinking - Part 1
Project 1 - Graph basics
"""

__author__ = 'manuel'


import graphs as graphs


# Graph examples (global constants)
EX_GRAPH0 = {0: {1, 2}, 1: set([]), 2: set([])}

EX_GRAPH1 = {0: {1, 4, 5}, 1: {2, 6}, 2: {3}, 3: {0},
             4: {1}, 5: {2}, 6: set([])}

EX_GRAPH2 = {0: {1, 4, 5}, 1: {2, 6}, 2: {3, 7}, 3: {7}, 4: {1},
             5: {2}, 6: {}, 7: {3}, 8: {1, 2}, 9: {0, 3, 4, 5, 6, 7}}


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
        for to_node in xrange(num_nodes):
            if to_node != node_id:
                digraph[node_id] = to_node
    return digraph

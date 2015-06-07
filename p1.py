"""
Algorithmic Thinking - Part 1
Project 1 - Graph basics
"""

__author__ = 'manuel'


# Graph examples (global constants)
EX_GRAPH0 = {0: {1, 2}, 1: set([]), 2: set([])}

EX_GRAPH1 = {0: {1, 4, 5}, 1: {2, 6}, 2: {3}, 3: {0},
             4: {1}, 5: {2}, 6: set([])}

EX_GRAPH2 = {0: {1, 4, 5}, 1: {2, 6}, 2: {3, 7}, 3: {7}, 4: {1},
             5: {2}, 6: {}, 7: {3}, 8: {1, 2}, 9: {0, 3, 4, 5, 6, 7}}

"""
    Disjoint Set data structure implementing the Union Find algorithm
"""

import networkx as nx 

class DisjointSet:
    """
        This is an implementation of the Disjoint Set datastructure within the context of Networkx graphs.

        disjointSet instances represent one set separated into a disjoint union of sets. All information other 
        than that necessary to represent connections between the elements of the represented set is stripped away.


        
    """

    def __init__(self):
        self.parents = {}

    
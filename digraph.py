# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 11:14:04 2022

@author: Alexa
"""

from edge import Edge
from node import Node

class Digraph:
    """Digraph Class"""
    
    def __init__(self):
        self.nodes = []
        self.edges = {}
    
        
    def add_node(self, node):
        if node in self.nodes:
            raise ValueError('The Node Already exists')
        else:
            self.nodes.append(node)
            self.edges[node] = []
    
    def add_edge(self, edge):
        src = edge.get_source()
        dest = edge.get_destination()
        if not (src in self.nodes or dest in self.nodes):
            raise ValueError('Node not in current graph')
        self.edges[src].append(dest)
        
    def InDegree(self, node):
       c = 0
       result = ''
       for src in self.nodes:
           for dest in self.edges[src]:
               if dest.get_name() == node.get_name():
                   c += 1
       result = result + 'The in-degree of ' + node.get_name() + ' is ' + str(c) + '\n'
       return result
                
    def OutDegree(self, node):
        c = 0
        result = ''
        for i in range(len(self.edges)):
            for i in self.edges[node]:
                c += 1
        result = result + 'The out-degree of ' + node.get_name() + ' is ' + str(c) + '\n'           
        return result
        

    def has_node(self, node):
        return node in self.nodes
    

    def __str__(self):
        result = ''
        r = ''
        for src in self.nodes:
            for dest in self.edges[src]:
                result = (f"{src.get_name():^12} ----> {dest.get_name():^12}\n")
                r += result
        return r
    
    def children_of(self, node):
        return self.edges[node]

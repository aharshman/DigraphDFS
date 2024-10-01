# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 11:17:53 2022

@author: Alexander Harshman
"""

from digraph import *

def DFS(graph, start, end, path, shortest, toPrint = False):
    """Assume graph is a digraph"""
    
    path = path + [start]
    
    if toPrint:
        print('Current Path is:', printpath(path))
        
    if start == end:  #Reaches the ends
        return path
    
    for node in graph.children_of(start):
        if node not in path:   #Avoids cycles
            if shortest == None or len(path) < len(shortest):
                newPath = DFS(graph, node, end, path, shortest, toPrint)
                
                if newPath != None:
                    shortest = newPath
                    
    return shortest


def printpath(path):
    """Assumes path is a list of nodes"""
    
    result = ' '
    for i in range(len(path)):
        result = result + str(path[i]) + ' ---> '
    result = result[:-6]
    
    return result



def testDFS():
    
    nodes = []

    for name in range(6): # Create 6 nodes

        nodes.append(Node(str(name)))

    g = Digraph()

    for n in nodes:

        g.add_node(n)

    g.add_edge(Edge(nodes[0], nodes[1]))

    g.add_edge(Edge(nodes[1], nodes[2]))

    g.add_edge(Edge(nodes[2], nodes[3]))

    g.add_edge(Edge(nodes[2], nodes[4]))

    g.add_edge(Edge(nodes[3], nodes[4]))

    g.add_edge(Edge(nodes[3], nodes[5]))
    
    g.add_edge(Edge(nodes[4], nodes[1]))
    
    g.add_edge(Edge(nodes[0], nodes[4]))

    g.add_edge(Edge(nodes[0], nodes[2]))

    g.add_edge(Edge(nodes[1], nodes[0]))

    g.add_edge(Edge(nodes[3], nodes[1]))

    g.add_edge(Edge(nodes[4], nodes[0]))
    
    sp = DFS(g, nodes[0], nodes[5], [], None, True)
    print('\nDFS shortest path is:', printpath(sp))
    
testDFS()
    
    
    
    
    
    
    